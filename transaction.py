class Transaction:
	"""	
	Transaction class outlines details captured in every ATM transaction
	A transaction can either be a withdrawal or deposit. 
	/*
	 	- In real life scenario, we'd capture date of the transaction
		so we can filter by date before enforcing validatios.	
	*/
	"""
	transaction_list = []
	
	# define our constructor
	def __init__ (self, balance, amount, method):
		self.balance = balance
		self.amount = amount
		self.method = method

        # save a new transaction
	def save_transaction(self):
		Transaction.transaction_list.append(self)

    	# revert a transaction
	def delete_transaction(self):
        	Transaction.transaction_list.remove(self)
	
	
	@classmethod
	def query_balance(cls):
		if len(Transaction.transaction_list) > 1:
			return Transaction.transaction_list[-1].balance
		else:
			return Transaction.transaction_list[0].balance
		
	
        # return a a number of deposits made today
	@classmethod
	def number_of_deposits(cls):
		numbers = []
		return len( [ item for item in cls.transaction_list if item.method == "deposit" ] ) 
	
	# number of withdraws made today - returns a number
	@classmethod
	def number_of_withdrawals(cls):
		"""
		calculate the length of a list with today's transactions whose method's flag was 'withdrawal'
		"""
		withdrawals = len( [ item for item in cls.transaction_list if item.method == "withdraw" ] ) 
		print(withdrawals)

		return withdrawals

        #  Calculate cummulative amount of cash withdrawn today
	@classmethod
	def amount_withdrawn_today(cls):
		"""	
		Run through transactions made today with flag 'withdraw' and calculate sum of the amounts.
		"""
		amount = sum( [ item.amount for item in cls.transaction_list if item.method=="withdraw"  ] )
		return amount

        #  Calculate amount of cash deposited today
	@classmethod
	def amount_deposited_today(cls):
		"""	
		Run through transactions made today with flag 'deposit' and calculate sum of the amounts.
		"""
		amount = sum( [ item.amount for item in cls.transaction_list if item.method=="deposit"  ] )
		return amount

    















