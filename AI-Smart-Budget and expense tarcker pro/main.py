import os
import smtplib
import time
import random
import mysql.connector
from dotenv import load_dotenv

from verification import verify_email
from AIinte import Aiintegration


load_dotenv()


# Session variables
current_user = None
incomes = None


# ================= DATABASE ================= #

def get_db_connection():

    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=int(os.getenv("DB_PORT"))
    )


# ================= START ================= #

def startingintro():

    print("Welcome to AI Smart Budget Tracker")
    time.sleep(2)

    print("1) Login")
    print("2) Register")

    choice = int(input("Enter choice: "))

    if choice == 1:
        login()

    elif choice == 2:
        registeration()

    else:
        print("Invalid choice")


# ================= REGISTER ================= #

def registeration():

    name = input("Enter name: ")
    dob = input("Enter DOB: ")
    email = input("Enter email: ")

    otp = random.randint(1000, 9999)

    sendingemail(otp, email)

    user_otp = int(input("Enter OTP: "))

    if otp == user_otp:

        insertrecord(name, dob, email)

        print("Registration successful. Please login.")
        startingintro()

    else:
        print("OTP failed")
        startingintro()


# ================= LOGIN ================= #

def login():

    global current_user

    email = input("Enter email: ").strip().lower()

    if not verify_email(email):
        print("Email not found.")
        startingintro()
        return

    otp = random.randint(1000, 9999)

    sendingemail(otp, email)

    for _ in range(3):

        try:
            user_otp = int(input("Enter OTP: "))
        except:
            continue

        if user_otp == otp:
            current_user = email
            print("Login successful")
            options()
            return

        print("Wrong OTP")

    print("Too many attempts")


# ================= OPTIONS ================= #

def options():

    global incomes

    income = int(input("Enter income: "))
    incomes = income

    currency = input("Currency: ")

    emi = int(input("EMI (0 if none): "))

    leftover = income - emi

    userfinancialdata(income, currency, emi, leftover)

    realoptions(income)


def realoptions(amount):

    print("""
1) Financial Strategy
2) Monthly Expense
3) Show Expenses
4) AI Strategy
""")

    ch = int(input("Choose: "))

    if ch == 1:
        financialstrat(amount)

    elif ch == 2:
        monthlyexpenditure()

    elif ch == 3:
        spendamt()

    elif ch == 4:
        Aiintegration()


# ================= EXPENSE ================= #

def monthlyexpenditure():

    global current_user, incomes

    spent = int(input("Spent: "))
    item = input("Item: ")
    date = input("Date: ")

    percent = (spent * 100) / incomes

    con = get_db_connection()
    cur = con.cursor()

    sql = """
    INSERT INTO expenditure(dates, spent, item, emailid, percentage)
    VALUES (%s, %s, %s, %s, %s)
    """

    cur.execute(sql, (date, spent, item, current_user, percent))

    con.commit()

    cur.close()
    con.close()

    print("Saved")


def spendamt():

    global current_user

    con = get_db_connection()
    cur = con.cursor()

    sql = "SELECT * FROM expenditure WHERE emailid=%s"

    cur.execute(sql, (current_user,))

    rows = cur.fetchall()

    cur.close()
    con.close()

    for r in rows:
        print(r)


# ================= EMAIL ================= #

def sendingemail(otp, useremail):

    sender = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("EMAIL_PASSWORD")

    msg = f"Your OTP is {otp}"

    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()

    server.login(sender, password)

    server.sendmail(sender, useremail, msg)

    server.quit()


# ================= DATABASE INSERT ================= #

def insertrecord(name, dob, email):

    con = get_db_connection()
    cur = con.cursor()

    sql = "INSERT INTO userrecord(name,dob,emailid) VALUES(%s,%s,%s)"

    cur.execute(sql, (name, dob, email))

    con.commit()

    cur.close()
    con.close()


def userfinancialdata(income, currency, emi, amount):

    global current_user

    con = get_db_connection()
    cur = con.cursor()

    sql = """
    INSERT INTO userfinancialdata
    (emailid,income,currency,emi,amountavailable)
    VALUES(%s,%s,%s,%s,%s)
    """

    cur.execute(sql, (current_user, income, currency, emi, amount))

    con.commit()

    cur.close()
    con.close()


# ================= STRATEGY ================= #

def financialstrat(amount):

    print("4 Bucket System")

    print("Survival:", amount * 0.5)
    print("Safety:", amount * 0.1)
    print("Growth:", amount * 0.3)
    print("Enjoyment:", amount * 0.1)

    realoptions(amount)


# ================= RUN ================= #

if __name__ == "__main__":
    startingintro()
