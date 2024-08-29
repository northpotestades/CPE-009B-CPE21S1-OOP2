class ATM():
    def __init__(self,serial_number,amount,history):
        self.serial_number=serial_number
        self.amount=amount
        self.history=history
    
    def deposit(self,account,amount):
        account.current_balance=account.current_balance+amount
        print("Deposit Complete")
        
    def withdraw(self,account,amount):
        account.current_balance=account.current_balance-amount
    
    def check_currentbalance(self,account):
        print("Balance:",account.current_balance)
        
    def view_transactionsummary(self):
        print(f'History: User {self.history} {self.amount}')