
deposit_amount = float(input("Enter the amount to deposit: "))
withdraw_amount = float(input("Enter the amount to withdraw: "))

class Bank:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        print("Depositing amount: ", deposit_amount)
        self.balance += deposit_amount

    def withdraw(self, amount):
        print("Withdrawing amount: ", withdraw_amount)
        self.balance -= withdraw_amount

balance = 0
bank = Bank(balance)
bank.deposit(deposit_amount)
bank.withdraw(withdraw_amount)
