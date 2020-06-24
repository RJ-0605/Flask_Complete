
import pymysql

mydb = pymysql.connect(
  host="localhost",
  user="root",
  passwd=""
)

databaselist=[]


mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

  
  (databaselist).append(x)



print(databaselist)

# temporary provisionary fix for checking and creating a specific database 
# there would be ofcourse future modifications 
# but for now just follow the syntax 
if ('myfirstdatabasef',) not in databaselist:
	mycursor.execute("CREATE DATABASE myfirstdatabasef")
else:
	'Done'
