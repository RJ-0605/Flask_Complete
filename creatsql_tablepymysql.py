
import pymysql

mydb = pymysql.connect(
  host="localhost",
  user="root",
  passwd="",
  database="firstdatabase"
)

tablelist=[]

# mycursor.execute("DROP TABLE customers")   this command comes after instance have been generated 
# to delete or drop the table we can also use the same format
# after connection has been made to delete the database itself

mycursor = mydb.cursor()

# these steps are necessary to delete a table 
# mycursor.execute("ALTER TABLE RegisterAccount DISCARD TABLESPACE;")

# mycursor.execute("DROP TABLE  RegisterAccount;")
mycursor.execute("SHOW TABLES")


# mycursor.execute("ALTER TABLE RegisterAccount DISCARD TABLESPACE;")

# mycursor.execute("DROP TABLE  RegisterAccount;")

# mycursor.execute("CREATE TABLE RegisterAccount(id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, firstname VARCHAR(80) NOT NULL, lastname VARCHAR(80) NOT NULL, email VARCHAR(100) NOT NULL, username VARCHAR(50) NOT NULL,dateofbirth VARCHAR(50) NOT NULL, password VARCHAR(255) NOT NULL )")



for x in mycursor:
  print(x)

  
  (tablelist).append(x)



print(tablelist)

# temporary provisionary fix for checking and creating a specific database 
# there would be ofcourse future modifications 
# but for now just follow the syntax 

# if ('usermessages',) not  in databaselist:
	# mycursor.execute("CREATE TABLE Blogtable(id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, title VARCHAR(80) NOT NULL, blogcomments VARCHAR(2500) NOT NULL, username VARCHAR(50) NOT NULL, image VARCHAR(255) NOT NULL )")
# else:


	# print ('Done')


if ('UserMessages') not  in tablelist:
	mycursor.execute("CREATE TABLE UserMessages(id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, UserType VARCHAR(80) NOT NULL, UserEmail VARCHAR(80) NOT NULL, Message VARCHAR(2500) NOT NULL )")
else:


	print ('Done')