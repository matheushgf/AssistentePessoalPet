import pymysql.cursors

def conecta():

    conexao = pymysql.connect(

        host='',

        user='',

        password='',

        db='',

        charset='',

        cursorclass=pymysql.cursors.DictCursor

    )

    try:

        yield conexao

    finally:

        conexao.close()