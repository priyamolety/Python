from pprint import pprint

class Account:
	def __init__(self,name,phno,acc_no,bal):
		self.name = name
		self.phno = phno
		self.acc_no = acc_no
		self.bal = bal

	def deposit(self,amt):
		self.bal += amt

	def withdraw(self,amt):
		self.bal -= amt

	def get_bal(self):
		print(f"The current balance is: {self.bal}")

	def details(self):
		print(f"Name: {self.name}"), 
		print(f"Phone Number: {self.phno}") 
		print(f"Account number = {self.acc_no}")
		print(f"Balance = {self.bal} \n")





