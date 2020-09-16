from acc import Account

reg = {}

print ("Welcome to the Commonbank")

while True:
	op = input("Choose one of the services \n\
		1. Open bank account \n\
		2. Withdraw from account \n --->")

	if op == "1":
		namee = input("Name:")
		ph_noo = input("Phone Number:")
		acc_noo = input("Account number:")
		ball = float(input("Initial balance:"))

		acc = Account(namee,ph_noo,acc_noo,ball)

		reg[acc_noo] = acc

	elif op == "2":
		acc_noo = input("enter account number ")
		amtt = float(input("amt to be withdrawn "))

		acc = reg[acc_noo]
		acc.withdraw(amtt)
		acc.details()

	else:
		break