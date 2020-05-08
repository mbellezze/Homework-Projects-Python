#For this challenge, create a bank account class that has two attributes:

#    owner
#    balance

#and two methods:

#    deposit
#    withdraw

#As an added requirement, withdrawals may not exceed the available balance.

#Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't 
# be overdrawn.


class Account:
    
    def __init__(self, owner, balance):

        self.owner = owner
        self.balance = balance
    
    def deposit(self, money_in):
        
        if(money_in<=0):
            print("No ha depositado nada")
        elif(money_in>0 and money_in<5000):
            self.balance += money_in
            print("Deposito aceptado")
        else:
            print("No puede depositar mas de $5000, pida una extensión")

    def withdraw(self, money_out):
        
        if((self.balance - money_out)<0):
            print("Fondos insuficientes")
        elif((self.balance - money_out)>0):
            self.balance -= money_out
            print("Extraccion aceptada")
        



# 1. Instantiate the class

acct1 = Account('Jose',100)


# 2. Print the object

print(acct1)


# 3. Show the account owner attribute

print(f"Account owner:   {acct1.owner}")

#'Jose'


# 4. Show the account balance attribute

print(f"Account balance: ${acct1.balance}")

#100


# 5. Make a series of deposits and withdrawals
acct1.deposit(50)
print(f"Account balance: ${acct1.balance}")
#Deposit Accepted


acct1.withdraw(75)
print(f"Account balance: ${acct1.balance}")
#Withdrawal Accepted


# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)

#Funds Unavailable!

#Good job!"""