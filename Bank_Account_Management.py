'''
Pair-2
Sümeyye KORKMAZ
Fatma Büşra TİLKİ
Ayşenur GÖKÇE
Aslı YILMAZ

'''

class Account:
    def __init__(self,account_holder,account_number,balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def set_balance(self,new_balance):
        self.__balance=new_balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} TL deposited. Current balance : {self.__balance} TL")

        else:
            print("Invalid amount")

    def withdraw(self,amount):
        if 0 < amount <=self.__balance:
            self.__balance -= amount
            print(f"{amount} TL withdraw. Current balance :{self.__balance} TL")

        else:
            print("Insufficient balance or invalid amount")

    def show_balance(self):
        print(f"Account  Holder : {self.account_holder} , Balance : {self.__balance} TL")



class CheckingAccount(Account):
    pass 


class SavingAccount(Account):
    def __init__ (self, account_holder,account_number, balance, interest_rate):
        super().__init__(account_holder, account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest (self):
        current_balance = self.get_balance()
        interest_amount=current_balance * self.interest_rate /100
        print(f" Interest added to account : {interest_amount} TL")
        self.set_balance(current_balance + interest_amount)

    def withdraw(self, amount):
        print("Withdrawals from saving account are limited.")
        super().withdraw(amount)



account1 = CheckingAccount ("Sümeyye Korkmaz", "0001", 1000)
account1.show_balance()
account1.deposit(500)
account1.withdraw(400)


account2 = SavingAccount("Ali Kaya", "0002", 2000, 5)
account2.show_balance()
account2.calculate_interest()
account2.show_balance()
account2.withdraw(500)
