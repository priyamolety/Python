from datetime import datetime
from tabulate import tabulate

rate = {}

class Ticket:
	def __init__(self,id):
		self.id = id 
		self.vehicle_type = input("Enter vehicle type 2w/4w: ")
		self.start_time = datetime.now()
		print(self.start_time)
		self.vehicle_no = input("enter vehicle number: ").upper()
		self.price = 0.0
		self.status = True
		self.total = 0.0

	def checkout(self):
		self.end_time = datetime.now()
		print(self.end_time)
		diff = self.end_time - self.start_time 
		print(diff)
		self.total_seconds = diff.total_seconds()
		print(self.total_seconds)


	def Calculate_rate(self,rate_card):
		rate = rate_card[self.vehicle_type]
		price = self.total_seconds * rate
		print(f"total amount: Rs. {price} ")



class Parking:
	def __init__(self):
		self.current_id = 1
		self.tw_slots = input("Enter the 2 wheeler slots: ")
		self.fw_slots = input("enter the 4 wheeler slots ")
		self.tw_used = 0
		self.fw_used = 0
		self.tw_rate = float(input("Enter rate/second for 2W: "))
		self.fw_rate = float(input("Enter rate/second for 4W: "))
		self.open_ticket = {}
		self.closed_tickets = {}


	def checkin(self):
		ticket = Ticket(self.current_id)
		self.current_id += 1
		self.open_ticket[ticket.id] = ticket 

	def checkout(self):
		ticket_id = int(input("Enter the ticket id: "))
		ticket = self.open_ticket[ticket_id]
		ticket.checkout()
		price = ticket.Calculate_rate({'2': self.tw_rate, '4':self.fw_rate})

		

		del self.open_ticket[ticket_id]
		self.closed_tickets[ticket_id] = ticket

	def all_open_tickets(self):
		data = []
		for tid,ticket in self.open_ticket.items():
			data.append([tid,ticket.vehicle_no,ticket.vehicle_type,ticket.start_time])
		print("ID Vehicle type vehicle in time")
		table = tabulate(data)
		print(table)