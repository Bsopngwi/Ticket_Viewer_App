import tkinter as tk
import requests
from tkinter import*
from requests.structures import CaseInsensitiveDict

#functions
def clear_frame():
	for widgets in lower_frame.winfo_children():
		widgets.destroy()


def print_tickets(link):
	clear_frame()

	headers = CaseInsensitiveDict()
	headers["Authorization"] = "Basic QmFyYmFyYS5jLnNvcG5nd2lAdHR1LmVkdTpCYXJiMjAwMjAxIQ=="

	ticketscall=requests.get(link, headers=headers).json()
	tickets_data=requests.get(link, headers=headers).json()['tickets']
	count=requests.get("https://zccbsopngwi.zendesk.com/api/v2/tickets/count.json", headers=headers).json()['count']

	l=0
	go_back()
	for data in tickets_data:
		l +=0.03
		display2=tk.Label(lower_frame,text=f'Total Number of tickets requested: {count["value"]}',bg='#d3d3d3',font=3)
		display2.place(relx=0, rely=0.0)

		display4=tk.Label(lower_frame,text=f'Tickets ID:{data["id"]}  Subject:{data["subject"]}  Status:{data["status"]}  Created at:{data["created_at"]}',bg='#d3d3d3',font=3)
		display4.place(relx=0, rely=0.015+l)
	
	if ticketscall['meta']["has_more"]==True:

		button=tk.Button(canvas, text=''+ u'\u27aa',command=lambda:print_tickets(ticketscall['links']["next"]) )
		button.place(relx=0.95, rely=0.12, relwidth=0.07, relheight=0.04)


def get_login_info():
	clear_frame()

	Email=entrye.get()
	Password=entryp.get()

	if (Email =='Barbara.c.sopngwi@ttu.edu') and (Password =='Barb200201!'):
		api='https://zccbsopngwi.zendesk.com/api/v2/tickets.json \-v -u '+Email+':'+Password
		response=requests.get(api)
		status=response.status_code

		if status==200:
			for widgets in frame.winfo_children():
				widgets.destroy()
			enter_pressed()
		elif status==500:

			display=tk.Label(lower_frame,text="500 Internal Server Error",bg='#d3d3d3',font=5)
			display.place(relx=0, rely=0)

			canvas.mainloop()
		else:
			display=tk.Label(lower_frame,text="Service Unavailable",bg='#d3d3d3',font=5)
			display.place(relx=0, rely=0)
			canvas.mainloop()
	else:
		display=tk.Label(lower_frame,text="Incorrect UserID Enter A Correct One",bg='#d3d3d3',font=5)
		display.place(relx=0, rely=0)

		canvas.mainloop()


def showatickets(ticket):
	clear_frame()
	url = "https://zccbsopngwi.zendesk.com/api/v2/tickets/"+ticket+".json \-v -u Barbara.c.sopngwi@ttu.edu:Barb200201!"
	headers = CaseInsensitiveDict()
	headers["Authorization"] = "Basic QmFyYmFyYS5jLnNvcG5nd2lAdHR1LmVkdTpCYXJiMjAwMjAxIQ==" 
	count=requests.get("https://zccbsopngwi.zendesk.com/api/v2/tickets/count.json", headers=headers).json()['count']
	resp = requests.get(url)
	if ticket.isdigit() ==True:
		if int(ticket) in range(1,count["value"]+1):
			if resp.status_code==200:
				resp2 = requests.get("https://zccbsopngwi.zendesk.com/api/v2/tickets/"+ticket+".json", headers=headers).json()['ticket']

				display2=tk.Label(lower_frame,text=f'Ticket ID: {resp2["id"]}',bg='#d3d3d3',font=3)
				display2.place(relx=0, rely=0.0)

				display4=tk.Label(lower_frame,text=f'Subject:{resp2["subject"]}  Status:{resp2["status"]}  Created at:{resp2["created_at"]}',bg='#d3d3d3',font=3)
				display4.place(relx=0, rely=0.04)

				go_back()
			else:
				display=tk.Label(lower_frame,text="Service Unavailable",bg='#d3d3d3',font=5)
				display.place(relx=0, rely=0)
				go_back()
		else:
			display=tk.Label(lower_frame,text="Incorrect ID Ticket",bg='#d3d3d3',font=5)
			display.place(relx=0, rely=0)
			go_back()
	else:
		display=tk.Label(lower_frame,text="Enter a number",bg='#d3d3d3',font=5)
		display.place(relx=0, rely=0)
		go_back()



def go_back():
	button4=tk.Button(canvas, text='go back', command=lambda:enter_pressed())
	button4.place(relx=0.8, rely=0.12, relwidth=0.07, relheight=0.04)

def enter_pressed():
	clear_frame()

	display=tk.Label(lower_frame,text="This is your Menu\n Choose among the option\n (Enter 1 for option 1)\n 1.Show all Tickets\n 2. Show a ticket\n 3. Quit",bg='#d3d3d3',font=5)
	display.place(relx=0.3, rely=0)

	entry2=tk.Entry(lower_frame,bg='white', width=10)
	entry2.place(relx=0.38, rely=0.2)

	button2=tk.Button(lower_frame, text="Enter",command=lambda:enter_pressed2(entry2.get()))
	button2.place(relx=0.5, rely=0.2)

											
def enter_pressed2(choice):
	choice=choice
	if choice =='1':
		link1="https://zccbsopngwi.zendesk.com/api/v2/tickets.json?page[size]=25"
		print_tickets(link1)
	elif choice =='2':
		clear_frame()

		display2=tk.Label(lower_frame,text="You choose to view a specific ticket \n Enter the ticket ID",bg='#d3d3d3',font=3)
		display2.place(relx=0, rely=0)

		entry3=tk.Entry(lower_frame,bg='white', width=20)
		entry3.place(relx=0.4, rely=0.1)

		button2=tk.Button(lower_frame, text="Enter",command=lambda:showatickets(entry3.get()))
		button2.place(relx=0.7, rely=0.1)
		go_back()
	elif choice=='3':
		clear_frame()

		canvas.destroy()
		exit()
	else:
		clear_frame()

		display2=tk.Label(lower_frame,text="Invalid Entry",bg='#d3d3d3',font=3)
		display2.place(relx=0, rely=0)

		go_back()





#User Interface
canvas=tk.Tk()
canvas=tk.Canvas(canvas,height=800,width=800)



canvas.pack() 
f=("poppins",10,"bold")

frame=tk.Frame(canvas,bg='white',bd=5)
frame.place(relx=0.14, rely=0.001, relwidth=0.7, relheight=0.12)


button=tk.Button(frame, text="Enter", command=lambda: get_login_info())
button.place(relx=0.9, rely=0.55, relwidth=0.08, relheight=0.2)

label=tk.Label(frame, text="Welcome To The Ticket Viewer Enter credential to view ticket",font=f,bg='white')
label.place(relx=0.05, rely=0.0, relwidth=0.8, relheight=0.6)

labele=tk.Label(frame, text="Email",font=f,bg='white')
labele.place(relx=0.0, rely=0.4, relwidth=0.4, relheight=0.2)

labelp=tk.Label(frame, text="Password",font=f,bg='white')
labelp.place(relx=0.4, rely=0.4, relwidth=0.4, relheight=0.2)


entrye=tk.Entry(frame, bg='white', width=5)
entrye.place(relx=0.05, rely=0.6, relwidth=0.3, relheight=0.25)


entryp=tk.Entry(frame, bg='white', width=2, show='*')
entryp.place(relx=0.5, rely=0.6, relwidth=0.3, relheight=0.25)


lower_frame=tk.Frame(canvas,bg='#d3d3d3',bd=10)
lower_frame.place(relx=0.0,rely=0.12, relwidth=1, relheight=1)




canvas.mainloop()









