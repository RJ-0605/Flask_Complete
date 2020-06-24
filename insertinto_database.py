
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="jedidiah",
  passwd="",
  database="firstdatabase"
)


 # create a cursor first to secure connection then one can then insert 
mycursor = mydb.cursor()

#   mycursor.execute("CREATE TABLE RegisterAccount(id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, firstname VARCHAR(80) NOT NULL, lastname VARCHAR(80) NOT NULL, email VARCHAR(100) NOT NULL, username VARCHAR(50) NOT NULL, password VARCHAR(255) NOT NULL )")


sql = "INSERT INTO RegisterAccount (firstname,lastname,username,email,password)VALUES (%s, %s , %s,%s,%s)"

val=('Rodney','Kwao','jedidiah','rodneytetteh@gmail.com','footb001')

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

