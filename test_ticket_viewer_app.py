import unittest
from requests.exceptions import Timeout
from unittest import TestCase
from unittest.mock import Mock

requests=Mock()

def print_tickets():

    json_data=requests.get('https://zccbsopngwi.zendesk.com/api/v2/tickets.json?page[size]=25')
    if json_data.status_code==200:
        return json_data.json()
    return None

def get_login_info():
    Email='Barbara.c.sopngwi@ttu.edu'
    Password='Barb200201'

    if (Email!='Barbara.c.sopngwi@ttu.edu') and (Password!='Barb200201!'):

        print("Incorrect UserID Enter A Correct One")
    else:
        return [Email,Password]

def get_login_info_api():
    json_data=requests.get('https://zccbsopngwi.zendesk.com/api/v2/tickets.json \-v -u Barbara.c.sopngwi@ttu.edu:Barb200201')
    if json_data.status_code==200:
       return 'Connected'
    return None

def showaticketsapi():
    api=requests.get("https://zccbsopngwi.zendesk.com/api/v2/tickets/10.json")
    if api.status_code==200:
       return 'Connected'
    return None


       
class TestTickets(unittest.TestCase):
    def test_print_tickets_retry(self):
        response_mock=Mock()
        response_mock.status_code=200
        response_mock.json.return_value={
        "tickets": [{
        "url": "https://zccbsopngwi.zendesk.com/api/v2/tickets/1.json",
        "id": 1,

        }]}

        requests.get.side_effect=[Timeout,response_mock]
        with self.assertRaises(Timeout):
            print_tickets()
        
        assert print_tickets()['tickets'][0]["id"] == 1
        
        assert requests.get.call_count == 2

class TectloginInfo(unittest.TestCase):
    def test_login_info(self):
        actual=get_login_info()
        expected=['Barbara.c.sopngwi@ttu.edu','Barb200201']
        self.assertEqual(actual,expected)

class Testinfoapi(unittest.TestCase):
    def test_loginInfoApi(self):
        response_mock=Mock()
        response_mock.status_code=200

        requests.get.side_effect=[Timeout,response_mock]
        with self.assertRaises(Timeout):
            get_login_info_api()
        
        assert get_login_info_api() =='Connected'
        
class Testshowticketsapi(unittest.TestCase):
    def test_showaticketApi(self):
        response_mock=Mock()
        response_mock.status_code=200

        requests.get.side_effect=[Timeout,response_mock]
        with self.assertRaises(Timeout):
            showaticketsapi()
        
        assert showaticketsapi() =='Connected'
               


if __name__ == '__main__':
    unittest.main()









