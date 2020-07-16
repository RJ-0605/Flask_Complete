
from flask import Flask, redirect, url_for, request, render_template,session
from validatorex import Register_validator , Login_validator

from flask_mysqldb import MySQL




app = Flask(__name__)

# must later genrate a sepearate function or import for generating 
# seperate key for session .

app.secret_key = '67fe0e4d2a60c56aac5b2362b1ded716'

# code for starting xampp  sudo /opt/lampp/lampp start
# 
# Database of MySQl with flask


#    these configurations helped with connecting xampp mysql server
#     with flask-mysqldb 

#  app.config['MYSQL_UNIX_SOCKET']='/opt/lampp/var/mysql/mysql.sock'    
#  app.config['MYSQL_PORT']=3306


#     Now all the SUPER USERS can be used interchangeably 

#     both this 

#     app.config['MYSQL_USER']='root'
#            and 
#     app.config['MYSQL_USER']='jedidiah'

#  as they are all using the xampp database
#  because of the socket provided



app.config['MYSQL_UNIX_SOCKET']='/opt/lampp/var/mysql/mysql.sock'
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_PORT']=3306
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='firstdatabase'
app.config['MYSQL_CURSORCLASS']='DictCursor'

app.config['upload_image']='./static/images/uploads'

mysql=MySQL(app)






posts = [
   {'author':'Corey Schafer',
    'title':'Blog post 1',
    'content':'First post content',
    'date_posted':'April 20,2018'

    },
    {
    'author':'Jane Doe',
    'title':'Blog post 2',
    'content':'Second post content',
    'date_posted':'April 21,2018'

    },
    {
    'author':'Aanet Doly',
    'title':'Blog post 3',
    'content':'Third post content',
    'date_posted':'April 27,2018'

    }
 
]

msg=""

@app.route('/')
@app.route('/home')
def home():
   if 'loggedin' in session :
      return render_template("index.html",post_variable=posts, username=session['username'])

   return redirect(url_for('login'))



# this is the new route created for the new blog bloginsert 




@app.route('/signupblog' )
def signupblog():

   # sideright=''
  return render_template("signupblog.html")

@app.route('/loginblog' )
def loginblog():

   # sideright=''
  return render_template("loginblog.html")


@app.route('/contactblog' )
def contactblog():
  if 'loggedin' in session :
    displaynoemail=True
    return render_template("contactblog.html",display='displaynoemail')
   # sideright=''
  return render_template("contactblog.html")


@app.route('/userfunc',methods = ['POST', 'GET'])
def userfunc():

  if 'email' in session :

    emailmsg=session['email']
    # return render_template("contactblog.html",display='displaynoemail')
 

  if request.method == 'POST':
    
    message=request.form.get('msg')
    usertype='Normal'
    
    if 'email' in session :
      usertype='Priority'
    else  :
      emailmsg=request.form.get('email')


      
    
    if emailmsg :
      cur = mysql.connection.cursor()
      sql = "INSERT INTO UserMessages (UserType,UserEmail,Message)VALUES (%s,%s,%s)"
      val=(usertype,emailmsg,message)

      cur.execute(sql, val)

      mysql.connection.commit()

      print(cur.rowcount, "record inserted.")



  return redirect(url_for('contactblog'))



@app.route('/bloginsert' )
def bloginsert():

   # sideright=''
  return render_template("BlogInsert.html")





@app.route('/blogdata' )
def blogdata():

  

 if 'loggedin' in session :

    cur = mysql.connection.cursor()
    cur.execute( 'SELECT * FROM  Blogtable')
    blogdetails=cur.fetchall()
    return render_template('BlogInsert.html',msg=msg,blogdetails=blogdetails)

 return render_template("BlogInsert.html")
  

@app.route('/admin' )
def admin():

  if 'adminpriv' in session :

     # sideright=''
    return render_template("admin.html")

  else:
    msg="you are not an admin"
    return msg





@app.route('/adminfunc', methods=['POST','GET'])
def adminfunc():

  msg=''

  if request.method == 'POST':
    image=request.files['bpicture']
    title=request.form.get('blogtitle')
    blogcomments=request.form.get('blogcomments')

    username='kobby'
    filename=image.filename
    image.save('./static/imgs/uploads/'+filename)
    imagesavdsucesful= True

    if imagesavdsucesful :

      cur = mysql.connection.cursor()

      sql = "INSERT INTO Blogtable (title,blogcomments,username,image)VALUES (%s, %s , %s,%s)"
      val=(title,blogcomments,username,filename)

      cur.execute(sql, val)

      mysql.connection.commit()

      print(cur.rowcount, "record inserted.")

    else:
      msg='Image not saved successful'

#these are outside they post so they work with the automatic get request
  # cur = mysql.connection.cursor()
  # cur.execute( 'SELECT * FROM  Blogtable')
  # blogdetails=cur.fetchall()

  return render_template('admin.html')







@app.route('/aboutinsert')
def aboutinsert():
   sideright=''
   return render_template("aboutinsert.html")


@app.route('/regfunc',methods = ['POST', 'GET'])
def regload():


   # redirect from the register function i set a variable here 
    # and catch it if it exists that is if 

   msg=''
   if request.method == 'POST':

      firstname = request.form.get('fname')
      lastname = request.form.get('lname')
      username = str(request.form.get('username'))
      date_ofbirth=str(request.form.get('birthday'))
      # date_ofbirth='bread'
      email = str(request.form.get('email')).lower()
      passwd = request.form.get('password')
      confirm_passwd = request.form.get('confirm_password')

      # we create a temporal  instance that can store the results from the validorex script  
      validated=Register_validator(firstname,lastname,username,email,passwd,confirm_passwd)
      
     # now we can access the function since the instance has been set 
      if validated.validator():

         # now about to crosscheck if username and email , data does not already exist in database before proceeding 
         cur = mysql.connection.cursor()

         # cur.execute('USE myfirstdatabase')

         cur.execute( 'SELECT * FROM  RegisterAccount WHERE username=%s  AND email=%s' , ( username , email,))
         account=cur.fetchone()

         cur.execute( 'SELECT * FROM  RegisterAccount WHERE username=%s ', ( username , ))
         uaccount=cur.fetchone()

         cur.execute( 'SELECT * FROM  RegisterAccount WHERE  email=%s' , (  email,))
         eaccount=cur.fetchone()

         if account or uaccount or eaccount :


            msg=f"An account with this username  {username} or email {email} already exists"
         
            # return redirect(url_for('register', reg_username=msg))

           # return render_template('register.html',reg_msg=msg)

            # else if there was no successful retrieval that means that information does not exist so we can add new input to the RegisterAccount
         else:

            sql = "INSERT INTO RegisterAccount (firstname,lastname,username,dateofbirth,email,password)VALUES (%s, %s , %s,%s,%s,%s)"

            val=(firstname,lastname,username,date_ofbirth,email,passwd)

            cur.execute(sql, val)

            mysql.connection.commit()

            print(cur.rowcount, "record inserted.")
            # redirect from the register function  to the login function 
            # i set a variable here 
             # and catch it if it exists that is if 
            msg=f"Account {username} created successfully "
            
            return render_template('loginblog.html', login_msg=msg)

         

      else:
         
         msg = "Please fill out form "
         #return redirect(url_for('register', reg_username=msg))
         
         
   return render_template('signupblog.html', reg_username=msg)






@app.route('/loginfunc',methods = ['POST'])
def loginload():



   if request.method == 'POST':

      usernamemail = str(request.form.get('usernam_email')).lower()
      
      passwd = request.form.get('password')

      # print("WORKS",usernamemail, passwd)

      # we create a temporal  instance that can store the results from the validorex script  
      validateduseremail = Login_validator(usernamemail,passwd) 

      
      
     # now we can access the function since the instance has been set 
      if validateduseremail.validator():
         cur = mysql.connection.cursor()

         # cur.execute('USE myfirstdatabase')

         # try fetching  from either username also try fetching from email , usernamemail in general refers to input that can hold both email    
    # and    username 
    # per what is given as an input 

         cur.execute( 'SELECT * FROM  RegisterAccount WHERE username=%s OR email=%s' , ( usernamemail , usernamemail, )  )
         ueaccount=cur.fetchone() 

         

         cur.execute( 'SELECT * FROM  RegisterAccount WHERE  password=%s' , (  passwd,))
         paccount=cur.fetchone()

            
         if  ueaccount and  paccount:
            cur.execute( 'SELECT username FROM  RegisterAccount WHERE username=%s OR email=%s' , ( usernamemail , usernamemail, )  )
            usnmaccount=cur.fetchone()
            
            # the username a key to generate the information 
            # there because i used Dictcursor property
            usn=usnmaccount['username']

            #  session begins here we can use the id of the the row that the ueaccount 
            # gave to us or the id that the password paccount gave to us 
            # since SELECT * picks the entire row where a particular column with a value is used to inspect.
            
            session['loggedin']=True
            session['id']= ueaccount['id']
            session['username']=ueaccount['username']
            session['email']=ueaccount['email']

            if session['username']=='admin':
              session['adminpriv']=True



            # return render_template("index.html",post_variable=posts, login_username=usn)
            return redirect(url_for('blogdata'))

         else:
            msg= "invalid login details "



      else:

         # this is thrown because of the LoginVlidator in validatorex
         msg= "invalid login syntax or login field is empty"





   return  render_template('login.html', login_msg=msg)






@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)

   session.pop('adminpriv', None)

   session.pop('email', None)
   # Redirect to login page
   return redirect(url_for('loginblog'))



















@app.route('/about')
def about():

#  return ("<h1>Hello World</h1>
   return render_template("about.html",title=about)

# this shows the main route url name i choose is independent of the function 
# just thst it helps in the future to make your work less complicated and helps you understand the linkage
#   url_for function helps you generate  the right url for the function logincheck 
# irrespective of the name change i made to 
#         make it logincheck

@app.route('/regcheckZ/<alertdiv>')
def regcheck(alertdiv):
   if alertdiv :
      
      return render_template("register.html",alertmssgs=alertdiv)

   else:
      return render_template("register.html")



@app.route('/register')
def register():

   return render_template("register.html")

@app.route('/login')
def login():

   return render_template("login.html")



@app.route('/success/<name>')
def success(name):
    
    return render_template("index.html")


# this will load future validator functions when the validator class 
# on seperate python script has been imported here
   







     

if __name__ == '__main__':
   app.run(debug = True)
