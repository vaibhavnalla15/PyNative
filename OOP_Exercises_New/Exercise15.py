""" Encapsulation - Protecting Attributes: Implement a class Account with a private attribute balance and provide methods to deposit and withdraw safely, checking for sufficient funds. """

class Account:
    def __init__(self, balance = 0):
        self.__balance = balance    # Encapsulated the balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited: {amount}, New Balance: {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient Funds")
        else:
            self.__balance -= amount
            print(f"Withdraw: {amount}, Remaining Balance: {self.__balance} ")

acc = Account(150)
acc.deposit(50)
acc.withdraw(100)
acc.withdraw(100)      
acc.deposit(1000)
