import pymysql.cursors

#Conexão com a base de dados usando usuário específico para o mesmo.
try:
  mydb = pymysql.connect(host='localhost', user='petuser', password='', db = 'pipet', charset='utf8mb4')
  cursor = mydb.cursor(pymysql.cursors.DictCursor)
  print("Connected Database!")
except pymysql.MySQLError as err:
  print(e)
  sys.exit(0)

finally:
  mydb.close()

#cursor = mydb.cursor()
#query = ("MYQUERY")
#cursor.execute(query)