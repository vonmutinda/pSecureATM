import unittest

# import our test module
from transaction import Transaction

class TransactionTest(unittest.TestCase):
	"""
	TransactionTest is a test class for performing tests
	on Transaction module.
	"""

	#tearDown function
	def tearDown(self): 
		"""
		Before running a test, clear the existing test database
		"""
		Transaction.transaction_list = []

   	# test the setUp
	# Initial transaction is similar to  creating a new user
	def setUp(self):
		self.initial_record = Transaction(150000,0,'' )
		self.initial_record.save_transaction()

    # Initial test.
	def test__init__(self):
		self.assertEqual(self.initial_record.balance,150000)
		self.assertEqual(self.initial_record.amount,0)
		self.assertEqual(self.initial_record.method,'')
    

    # test is instance
	def test_instance(self):
		self.assertTrue( isinstance(self.initial_record,Transaction) )

    # ability to save a new transaction
	def test_can_save_transaction(self):
		self.another = Transaction(100,10,'withdraw')
		self.another.save_transaction()
		self.assertEqual(len(Transaction.transaction_list),2)
	
	# ability to delete a transaction from the database
	def test_can_delete_transaction(self):
		self.rolledback = Transaction(100,10,'deposit')
		self.rolledback.save_transaction()
		self.rolledback.delete_transaction()
		self.assertTrue(self.rolledback,None)
		
    # ability to query balance
	def test_can_query_balance(self):
		self.balance = Transaction.query_balance()
		self.assertEqual(self.balance,150000)

	# ability to check number of deposits made in a day
	def test_can_calculate_number_of_deposits(self):
		self.locked_savings = Transaction(100,10,'deposit')
		self.honeymoon_savings = Transaction(200,10,'deposit')
		self.locked_savings.save_transaction()
		self.honeymoon_savings.save_transaction()
		self.assertTrue( Transaction.number_of_deposits(),2 )


	# ability to check number of withdrawals made
	def test_can_calculate_number_of_withdrawals_made(self):
		self.emergency = Transaction(100,500,'withdraw')
		self.salary = Transaction(100,2000,'withdraw')
		self.emergency.save_transaction()
		self.salary.save_transaction()
		self.assertTrue( Transaction.amount_withdrawn_today(),2 )
		
	# ability to determine amount of cash deposited in a day
	def test_can_calculate_cumulative_deposit(self):
		self.one = Transaction(100,10,'deposit')
		self.two = Transaction(10,5,'deposit')
		self.one.save_transaction()
		self.two.save_transaction()	
		self.assertEqual( Transaction.amount_deposited_today(),15 )

	# Determine amount withdrawn in a day
	def test_can_calculate_cumulative_withdrawal(self):
		self.first = Transaction(100,10,'withdraw')
		self.second = Transaction(10,10,'withdraw')
		self.first.save_transaction()
		self.second.save_transaction()	
		self.assertEqual( Transaction.amount_withdrawn_today(),20 )

    
if __name__ == '__main__':
	unittest.main()
