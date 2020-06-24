
import mysql.connector
mydb = mysql.connector.connect(
	host="localhost",
	port="3306",
	user="root",
	passwd=""
	)
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE myfirstdatabase")
