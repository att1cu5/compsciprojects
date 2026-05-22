import socket
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
prefferedIPaddress="10.236.1.17"
def welcome():
    print("Welcome User to the Wonderful World of Wicked Banking.")
    print("WWWB is here to assist you in… (create a welcome statement and a bank name)")
    print("welcome statement: ")
    
def print_balance(balance):
    print(f"Your balance is ${balance:.2f}")


def withdraw(balance):
    print("How much do you want to withdraw? ")
    amount = float(input())
    if amount > balance:
        print("Beat it loser")
    else:
        balance -= amount
        print_balance(balance)


def deposit(balance):
    print("How much do you want to deposit? ")
    dep_amount = float(input())
    balance += dep_amount
    print_balance(balance)
    return balance

def main():
    account1 = 1000
    account2 = 0
    

    print_balance(account1)
    #print_balance(account2)


    account2=deposit(account1)
    
    
    withdraw(account2)
     
if(local_ip==prefferedIPaddress):
    if __name__ == "__main__":
        main()
else:
    print("Are you trying to get into my bank account? ")
    

