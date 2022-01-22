import mysql.connector as sql
conn = sql.connect(host='localhost',user='root',password='patel@rkp2004',database='KESCO')
if conn.is_connected():
    print("successfully connected")
c1=conn.cursor()
c1.execute('create table newuser(username VARCHAR(30) primary key,password VARCHAR(30),confirmpasswd VARCHAR(30))')
c1.execute('create table AddNewCustomer(accountno int primary key,name VARCHAR(25),address VARCHAR(100),areacode INT(6),phoneno INT(10),email VARCHAR(25),mid VARCHAR(25))')
c1.execute('create table Transaction(accountno INT(10) ,unit INT(10),today VARCHAR(25),totamt INT(10),GST INT(10),totalamt INT(10),p VARCHAR(25) , foreign key(accountno) references AddNewCustomer(accountno))')
print("table created")


