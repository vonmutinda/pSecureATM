from datetime import datetime

# import our classes
from transaction import Transaction


# start the program with 
CURRENT_BALANCE = 150000 # 150K

# deposit
MAX_DEPOSIT = 150000 # 150K
MAX_DEPOSIT_PER_TRANS = 40000 # 40K
MAX_DEPOSIT_FREQ = 4

# withdrawal
MAX_WITHDRAWAL = 50000 # 50K
MAX_WITHDRAWAL_PER_TRANS = 20000 # 20K
MAX_WITHDRAWAL_FREQ = 3

# our functions - Controllers or other 'views'

def check_balance():
	return Transaction.query_balance()
	

def deposit_amount(amount):
	if amount > MAX_DEPOSIT_PER_TRANS:
		print("Sorry! You've attempted to make a deposit exceeding KES 40,000. Kindly retry.")
		
	elif Transaction.number_of_deposits() > MAX_DEPOSIT_FREQ:
		print("Sorry! You've exceeded number of deposits per day. kindly try again tommorow")

	else:
		bal = Transaction.query_balance() + amount # calculate new balance
		new_trans = Transaction(bal, amount,'deposit')
		new_trans.save_transaction() # Save changes

		if Transaction.amount_deposited_today() > MAX_DEPOSIT:
			print("Dear customer, limit deposit per day is KES 150,000. We apologise for the inconvinience")
			new_trans.delete_transaction()
		else:
			print("-"*70)
			print("Deposit successful! New balance is: KES {}".format( Transaction.query_balance() ))


def withdraw_amount(amount):
	# if the customer attempts to withdraw above specified withdrawal limit

	if amount > MAX_WITHDRAWAL_PER_TRANS:
		print("Error: Attempted to make a withdrawal above KES 20,000" )

	elif Transaction.number_of_withdrawals() > MAX_WITHDRAWAL_FREQ:
		print("Exceeded number of withdrawals. Please try again tomorrow.")
	
	else:
		balance = Transaction.query_balance() - amount
		new_trans = Transaction(balance,amount, 'withdraw')
		new_trans.save_transaction()

		if Transaction.amount_withdrawn_today() > MAX_WITHDRAWAL:
			new_trans.delete_transaction()
			print("Exceeded amount of deposit in a day! Your Balance is KES {}".format( Transaction.query_balance() ))
		else:
			print("-"*70)
			print("Withdrawal successful! New balance is: KES {}".format( Transaction.query_balance() ))

"""
	Our main program
"""

def main():
	
	# Assuming we fetching data about logged in user
	# We instantiate a new class of transaction
	new_record = Transaction(CURRENT_BALANCE,0,'')
	new_record.save_transaction()

	while True:
		print("-"*70)

		print ("Welcome to pSecure ATM ! pesa Mkononi.")

		print("-"*70)

		print("""
            	Select an option :
            	[1] . Balance
            	[2] . Deposit
	    		[3] . Withdrawal
            	[4] . Exit 
        	""")
		
		# capture user's option
		option = input(">")
		
		# Logic for showing balance
		if str(option) == "1":
			bal = check_balance()
			print("Dear Customer, your balance is KES {}".format(bal))
			
		# Enable user to make deposit
		elif str(option) == "2":
			print("Enter amount to deposit : ")
			amount = input(">")
			
			# call deposit method
			deposit_amount( int(amount) )

		# Withdraw amount option
		elif str(option) == "3":
			print("Enter amount to withdraw : ")
			amount = input(">")
			
			# call deposit method
			withdraw_amount(int(amount))
		
		# logic for exiting the code
		elif str(option) == "4":
			print("-"*70)
			print("Logged out! Thank you for stopping by!")
			print("-"*70)
			break
		
		# If user's options are not recognised
		else:
                    print("-"*70)
                    print("Sorry ! Connection problem or invalid MMI code!")
			
	




if __name__ == '__main__':
    
    main()
