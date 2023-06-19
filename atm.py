#program for ATM MACHINE
import mysql.connector

#connecting python with sql database
connector=mysql.connector.connect(host="localhost",user="root",password="Sreeganga@123",database="atm")
 
 #creating a cursor object
cursor=connector.cursor()

#executing the mysql quary
cursor.execute("create table if not exists account (name varchar(30),pin varchar(30),balance float)")
connector.commit()


#function defenition for creating an account
def create_account():
    name=input("enter the name:")
    pin=input("enter the pin:")
    balance=float(input("enter the required balance of the account:"))
    cursor.execute("insert into account (name,pin,balance) values ('{}','{}','{}')".format(name,pin,balance))
    connector.commit()
    print("Account Created Successfully")
    print(f"==========WELCOME Mr/Mrs {name}==========")

    return True


#function defenition for login to the account
def login():
    name=input("enter the name:")
    pin=input("enter the pin:")
    cursor.execute("select * from account where name='{}'".format(name))
    account=cursor.fetchone()
    if account is not None:
        name,entered_pin,balance=account
        if entered_pin==pin:
            print("Login Successfull")
            print(f"==========WELCOME Mr {name}==========")
            return name
        else:
            print("Incorrect Pin,Try again")
            return None
            
    else:
        return None


#function defenition for depositing money to the account
def deposit(account_id):
    amount=float(input("enter the amount to be deposited:"))
    cursor.execute("select balance from account where name='{}'".format(account_id))
    current_balance=cursor.fetchone()[0]
    new_balance=current_balance+amount
    cursor.execute("UPDATE account set balance='{}' where name='{}'".format(new_balance,account_id))
    connector.commit()
    print("Deposit Successfully")
    print(f"Your Balance:{new_balance}")
    return new_balance


#function defenition for withdrawing money from the account
def withdraw(account_id):
    amount=float(input("enter the amount to be withdrawed:"))
    cursor.execute("select balance from account where name='{}'".format(account_id))
    current_balance=cursor.fetchone()[0]
    if current_balance>=amount:
        new_balance=current_balance-amount
        cursor.execute("UPDATE account set balance='{}' where name='{}'".format(new_balance,account_id))
        connector.commit()
        print("Withdraw Successfully")
        print(f"Your Balance:{new_balance}")
        return new_balance
    else:
        print("Insufficient Balance")
        return None


#function defenition for checking balance of the account
def check_balance(account_id):
    cursor.execute("select balance from account where name='{}'".format(account_id))
    current_balance=cursor.fetchone()[0]
    print(f"Your Balance:{current_balance}")
    return current_balance       


#presenting the opening page of the ATM Machine
while True:
    print("=======ATM MACHINE=======")
    print("1.Create account")
    print("2.Login")
    print("3.Exit")

    choice=input("enter the choice(1-3):")

#imputing the users choice 
    if choice=="1":
        create_account()
    elif choice=="2":
        account_id=login()
        if account_id:
            print("======ACCOUNT MENU======")
            print("1.Deposit")
            print("2.Withdraw")
            print("3.Check Balance")
            print("4.Logout")
            choice=input("enter the choice(1-4):")
            if choice=="1":
                deposit(account_id)
            elif choice=="2":
                withdraw(account_id)
            elif choice=="3":
                check_balance(account_id)
            elif choice=="4":
                break
            else:
                print("Invalid Choice")
        else:
            print("Account not found")
    elif choice=="3":
        print("Thanks for Coming❤️❤️")
        break
    else:
        print("Invalid Choice,Try again")
cursor.close()


