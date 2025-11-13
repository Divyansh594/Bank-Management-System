import mysql.connector as a

# Database connection
con = a.connect(host="localhost", user="root", passwd="1234", database="bank")


def openAcc():
    ac = int(input("Enter Account No: "))
    n = input("Enter Name: ")
    db = input("Enter D.O.B: ")
    ad = input("Enter address:")
    p = int(input("Enter Phone :"))
    ob = int(input("Enter Opening Balance :"))

    data1 = (ac, n, db, ad, p, ob)
    data2 = (ac, n, ob)

    sql1 = 'insert into account values (%s, %s, %s, %s, %s, %s)'
    sql2 = 'insert into amount values (%s, %s, %s)'

    c = con.cursor()
    c.execute(sql1, data1)
    c.execute(sql2, data2)
    con.commit()

    print("Data Enter Successfully")
    MainMenu()


def depoAcc():
    am = int(input("Enter Amount:"))
    accno = int(input("Enter Account No:"))

    a_sql = "select balance from amount where accno=%s"
    data = (accno,)

    c = con.cursor()
    c.execute(a_sql, data)
    myresult = c.fetchone()
    tam = myresult[0] + am

    sql = "update amount set balance = %s where accno = %s"
    d = (tam, accno)
    c.execute(sql, d)
    con.commit()

    print("Amount Deposited Successfully")
    MainMenu()


def withAm():
    am = int(input("Enter Amount:"))
    accno = int(input("Enter Account No:"))

    a_sql = "select balance from amount where accno=%s"
    data = (accno,)

    c = con.cursor()
    c.execute(a_sql, data)
    myresult = c.fetchone()
    tam = myresult[0] - am

    sql = "update amount set balance = %s where accno = %s"
    d = (tam, accno)
    c.execute(sql, d)
    con.commit()

    print("Amount withdrawl Successfull")
    MainMenu()


def balance():
    accno = input("Enter Account No: ")
    a_sql = "select balance from amount where accno=%s"
    data = (accno,)

    c = con.cursor()
    c.execute(a_sql, data)
    myresult = c.fetchone()
    print("Balance for Account : ", accno, " is ", myresult[0])
    MainMenu()


def dispAcc():
    accno = input("Enter Account No : ")
    a_sql = "select * from account where accno = %s"
    data = (accno,)

    c = con.cursor()
    c.execute(a_sql, data)
    myresult = c.fetchone()
    for i in myresult:
        print(i, end=" ")
    print()
    MainMenu()


def closeAcc():
    accno = input("Enter Account No: ")
    sql1 = "delete from account where accno = %s"
    sql2 = "delete from amount where accno=%s"
    data = (accno,)

    c = con.cursor()
    c.execute(sql1, data)
    c.execute(sql2, data)
    con.commit()
    MainMenu()


def MainMenu():
    print("*" * 140)
    print("BANK MANAGEMENT SYSTEM".center(140))
    print("1.OPEN NEW ACCOUNT".center(140))
    print("2.DEPOSIT AMOUNT".center(140))
    print("3.WITHDRAW AMOUNT".center(140))
    print("4.BALANCE ENQUIRY".center(140))
    print("5.DISPLAY CUSTOMER DETAILS".center(140))
    print("6.CLOSE AN ACCOUNT".center(140))
    print("*" * 140)


if __name__ == "__main__":
    MainMenu()
    while True:
        try:
            choice = int(input("Enter Task No"))
        except ValueError:
            print("wrong task no")
            MainMenu()
            continue

        if choice == 1:
            openAcc()
        elif choice == 2:
            depoAcc()
        elif choice == 3:
            withAm()
        elif choice == 4:
            balance()
        elif choice == 5:
            dispAcc()
        elif choice == 6:
            closeAcc()
        else:
            print("wrong task no")
            MainMenu()