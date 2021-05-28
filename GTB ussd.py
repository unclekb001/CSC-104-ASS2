# def return_to_menu():
# 	print("welcome to GTBANK bank ussd transaction")
# 	ussd_code = int(input("Enter ussd code here: "))
def back():
	if len(pin) == 4:
		print('your account balance is',balance,'Naira')
while True:
	list_of_accont_name = ['PYTHON']
	list_of_accont_number = []
	account_pin = 2021
	balance = 787000000
	ussd_code = input("Enter ussd code here: ")
	if ussd_code == '*737#':
		print('GTBANK')
		print("1.Airtime self\n2.Airtime others\n3.Transfer GTBANK banks\n4. Transfer other.")
		option = int(input('select option:'))
		if option == 1:
			pin = input('Enter your pin')
			if len(pin) == 4:
				amount = int (input('Please enter amount:'))
				print('Transaction succeful')
				break
			else:
				print('Wrong pin')
				pin = input('Enter pin to continue:')
				back()
			break
		elif option == 2:
			pin = input('Enter your pin')
			if len(pin) ==4:
			   	amount = int(input('Enter amount:'))
			   	int (input('please enter destination phone number:'))
			   	print('Transaction succeful')
			   	break
			else:
				print('Wrong pin')
				pin = input('Enter pin to continue:')
				back()
			break
		elif option==3:
			pin = input('Enter your pin')
			if len(pin) ==4:
				amount = int(input('Enter amount:'))
				int (input('please enter your GTB account number:'))
				print('Transaction succeful')
				break
			else:
				print('Wrong pin')
				pin = input('Enter pin to continue:')
				back()
			break
		elif option==4:
			pin = input('Enter your pin')
			if len(pin) ==4:
				int (input('please enter account number of the beneficiary'))
				amount = int(input('Enter amount:'))
				print('select bank')
				print("1.Access bank\n2.City bank nig limited\n3.Eco bank Nigeria plc\n4.FidelityBank plc.")
				option = int(input('select option:'))
				if option == 1:
					pin = input('Enter your pin')
					if len(pin) == 4:
						print('Transaction succeful')
				elif option == 2:
					pin = input('Enter your pin')
					if len(pin) == 4:
						print('Transaction succeful')
				elif option == 3:
					pin = input('Enter your pin')
					if len(pin) == 4:
						print('Transaction succeful')
				elif option == 4:
					pin = input('Enter your pin')
					if len(pin) == 4:
						print('Transaction succeful')
					break
			else:
				print('Wrong pin')
				pin = input('Enter pin to continue:')
				back()
			break