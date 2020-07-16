


class Database:
	def __init__(self,mysql):
		self.mysql=mysql
		self.db=self.mysql.connection
		self.cur=self.db.cursor()


	def get_all(self,tb_name):
		#alternatively we could write the first code below as it is or another way is beneath it 
		#self.cur.execute(SELECT * FROM %s , (str(tb_name),) )
		self.cur.execute('SELECT * FROM'+ tb_name +',')
