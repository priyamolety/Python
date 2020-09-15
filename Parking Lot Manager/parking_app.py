from Parking_lot_manager import Parking 

park = Parking() 

while True:
	op = int(input("1.Checkin a vehicle \n\
2. Checkout a vehile \n\
3. See the list of all parked vehicles \n -->"))
	if op == 1:
		park.checkin()
	elif op == 2:
		park.checkout()
	elif op == 3:
		park.all_open_tickets()
	else:
		break 