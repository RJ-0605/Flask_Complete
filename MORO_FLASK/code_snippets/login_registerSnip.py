# this will help throw a variable in te future that can be loaded to a screen from post 

@app.route('/logincheckZ/<alertdiv>')
def logincheck(alertdiv):
   if alertdiv :
      
      return render_template("register.html",alertmssgs=alertdiv)

   else:
      return render_template("register.html")



@app.route('/login')
def login():

   return render_template("register.html")



@app.route('/success/<name>')
def success(name):
    'welcome %s' % name
    return render_template("hello.html")


# this will load future validator functions when the validator class 
# on seperate python script has been imported here
@app.route('/loginfunc',methods = ['POST', 'GET'])
def loginload():
   if request.method == 'POST':
      user = request.form['fname']
      # in the near future i will write this into a class called validator and 
      # import its functions to verify for empty strings and what not , and min ,max value for strings
      if user == "cat" :
        return redirect(url_for('success',name = user))
      else:
          fldusrmsg="Wrong User name characters"

          return redirect(url_for('logincheck', alertdiv=fldusrmsg))
   else:
      user = request.args.get('fname')
      return redirect(url_for('success',name = user))