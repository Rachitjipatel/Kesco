import mysql.connector as sql, random, datetime as dt
import matplotlib.pyplot as plt

conn = sql.connect(host='localhost', user='root', passwd='patel@rkp2004', database='KESCO')
if conn.is_connected():
    print("successfully connected")
c = 'YES' or "yes" or 'Yes'
V = 'YES' or "yes" or 'Yes'
c1 = conn.cursor()
while c == 'YES' or "yes" or 'Yes':
    print('******************************************************************************')
    print('*            !!WELCOME TO KANPUR ELECTRICAL SUPPLY COMPANY!!                 *')
    print('*                  !!! WE ARE GLAD TO SERVE YOU !!!                          *')
    print('******************************************************************************')
    print(dt.datetime.now())
    print(' ______________________')
    print('|    1.  NEW USER      |')
    print('|    2.EXISTING USER   |')
    print('|    3.  EXIT          |')
    print('|______________________|')
    ch = int(input('ENTER YOUR CHOICE:'))
    if ch == 1:
        username = input("Enter your username:")
        password = input("Enter your password:")
        confirmpasswd = input("Confirm  your password:")
        if password == confirmpasswd:
            info1 = "insert into newuser values('{}','{}','{}')".format(username, password, confirmpasswd)
            c1.execute(info1)
            conn.commit()
            c = input("do you want to continue?(yes or no)")
        else:
            print('!Oops passwords do not match!')
            print('!Please Try again!')
            c = input("Do you want to continue?(yes or no)")
    elif ch == 2:
        username = input('Enter your username:')
        password = input('Enter your password:')
        info2 = "select * from newuser where username='{}' and password='{}'".format(username, password)
        c1.execute(info2)
        data = c1.fetchall()
        while V == 'YES' or "yes" or 'Yes':
            if any(data):
                print(' ________________________________')
                print('|     1.   ACCOUNT SETTINGS      |')
                print('|     2.VIEW CUSTOMER DETAILS    |')
                print('|     3.  TRANSACTIONS           |')
                print('|     4.GRAPHICAL REPRESENTATION |')
                print('|     5.        EXIT             |')
                print('|________________________________')
                ch1 = int(input('ENTER YOUR CHOICE'))
                if ch1 == 1:
                    print('1.NEW CUSTOMER')
                    print('2.DELETE EXISTING ACCOUNT')
                    ch2 = int(input('ENTER YOUR CHOICE:'))
                    if ch2 == 1:
                        accountno = random.randrange(1000000, 9999999, 10)
                        print("Your KESCO account_no is", accountno)
                        mid = input("enter your meter ID:")
                        name = input('Enter your name :')
                        address = input('Enter your address :')
                        areacode = int(input('Enter your area PIN CODE :'))
                        phoneno = int(input('Enter your PHONE NUMBER :'))
                        email = input('Enter your email :')
                        info2 = f"insert into AddNewCustomer values({accountno},'{name}','{address}',{areacode},{phoneno},'{email}','{mid}')"
                        print(info2)
                        c1.execute(info2)
                        conn.commit()
                        V = input("Do you want to continue?(yes or no):")
                        if V == 'yes':
                            continue
                        else:
                            break
                    elif ch2 == 2:
                        acc = input("ENTER YOUR ACCOUNT NUMBER:")
                        use = input("ENTER YOUR USERNAME:")
                        info6 = c1.execute("delete from Transaction where accountno='{}'".format(acc))
                        info7 = c1.execute("delete from AddNewCustomer where accountno='{}'".format(acc))
                        info8 = c1.execute("delete from newuser where username='{}'".format(use))
                        c1.execute(info6)
                        c1.execute(info7)
                        c1.execute(info8)
                        conn.commit()
                        print("THANK YOU FOR USING KESCO WEB ,YOUR ACCOUNT IS SUCCESFULLY DELETED")
                        V = input("Do you want to continue?(yes or no)")
                        if V == 'yes':
                            continue
                        else:
                            break



                elif ch1 == 2:

                    accountno = int(input('Enter your account number  :'))
                    info4 = "select * from AddNewCustomer where accountno=" + str(accountno)
                    c1.execute(info4)
                    data1 = c1.fetchall()
                    for row in data1:
                        print(" Account Number: ", row[0])

                        print("Person name:", row[1])
                        print("Your meter device ID=", row[6])
                        print("Residential address:", row[2])
                        print("area code:", row[3])
                        print("phone number:", row[4])
                        print("email:", row[5])
                    if V == 'yes':
                        continue
                    else:
                        break
                elif ch1 == 3:
                    accountno = int(input('Enter your account number  :'))
                    info10 = "select * from Transaction where accountno=" + str(accountno)
                    c1.execute(info10)
                    data3 = c1.fetchall()
                    print(data3)
                    for row in data3:
                        paid = row[6]
                    if paid == 'yes':
                        print('you have already paid the bill')
                        break
                    else:
                        unit = random.randint(0, 101)
                        print('Dear customer, you have used ', unit, 'units of electricity.')
                        print('One unit of curent is 6 rupees + 110 fixed charge amount')
                        amount = (6 * unit) + 110
                        today = dt.date.today()
                        deadline = dt.date(2020, 1, 30)
                        if deadline < today:
                            fine = (today - deadline) * 30
                            totamt = amount + fine
                            print('you have dealyed for ', today - deadline, 'days.The fine per day is 30 rupees.')
                            GST = (15 / 100) * totamt
                            totalamt = totamt + GST
                            print('Pleae payup ', totalamt, 'rupees inclding GST')
                            p = input("Please Enter YES to transact")
                            if p == "YES" or 'Yes' or 'yes':
                                print("Transaction successful")
                                print("You have paid the bill")
                            else:
                                print('plz pay the bill sooner')
                        else:
                            totamt = 0
                            GST = (15 / 100) * amount
                            totalamt = amount + GST
                            print('Pleae payup ', totalamt, 'rupees inclding GST')
                            p = input("Please Enter YES to transact")
                            if p == "YES":
                                print("Transaction successful")
                                print("You have paid the bill")
                            else:
                                print('plz pay the bill sooner')
                        info3 = "insert into Transaction values({},{},'{}',{},{},{},'{}')".format(accountno, unit,
                                                                                                  today,
                                                                                                  totamt, GST, totalamt,
                                                                                                  p)
                        c1.execute(info3)
                        conn.commit()
                        V = input("do you want to continue?(yes or no)")
                        if V == 'yes':
                            continue
                        else:
                            break
                elif ch1 == 4:
                    info9 = "select accountno,totalamt from Transaction"
                    c1.execute(info9)
                    L1, L2, = [], []
                    for i in c1.fetchall():
                        L1.append(i[0])
                        L2.append(i[1])
                    plt.plot(L1, L2)
                    plt.title("GRAPH")
                    plt.show()
                    V = input("do you want to continue?(yes or no)")
                    if V == 'yes':
                        continue
                    else:
                        break

                elif ch1 == 5:
                    print("THANK  YOU!!!!  VISIT AGAIN!!!!")
                    break
                    c = 'yes'


            else:
                print('username / password is incorrect')
                break
                c = input("Do you want to try again?(yes or no)")


        else:
            print("THANK  YOU!!!!  VISIT AGAIN!!!!")
            V = 'no'



    elif ch == 3:
        print("THANK YOU FOR USING OUR SERVICE !!!!!")
        c = 'no'
        break
    else:
        print("invalid choice")
        c = input("Do you want to try again?(yes or no)")
else:
    print("!!!!!!!THANKS FOR USING KESCO ONLINE SERVICE !!!!!!!")
    print("!!!!!!!HAVE A GREAT DAY ")

    c = 'no'



