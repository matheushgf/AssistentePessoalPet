import pymysql.cursors
from contextlib import contextmanager

table_map = {
    'user': {
        'usuario': ['id', 'nome', 'sexo', 'numero']
    },
    'pet': {
        'user_pet': ['id', 'nome', 'peso', 'raca', 'sexo']
    },
}

# CRUD - CREATE, READ, UPDATE, DELETE
'''                      >>>>>>>>>>>>>>> Bloco separado para teste futuro.<<<<<<<<<<<<<<<<<<<<<<<<,
# CONEXÃO COM O BANCO

def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='password',
        db='dbusado',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

try:
    yield conexao
finally:
    conexao.close()
'''
def get_table_fields (key_table):  #key_table chama a tabela no dicionário.
    for key in table_map:
        if key == key_table:
            return [ (k, table_map[key][k]) for k in table_map[key] ]  #Chama valores, de acordo com o nome descrito(tabela) no dicionário.

# INSERE UM REGISTRO NA BASE DE DADOS
def insert (key_table, reg_values):  #Colocar nome da tabela e valores, os comandos internos irão formatar e tratar os dados.
    with conecta() as conexao:
         with conexao.cursor() as cursor:

             table_fields = get_table_fields(key_table)[0]

             str_colum = ','.join([ '\"%s\"'.format(f) for f in table_fields[1] ])  #Insere o nome de cada coluna já formatado
                                            # Ex.: "id", "nome", "sexo", "numero"

             str_value = ','.join([ str(f) for f in reg_values ])  #Insere o nome de cada cado cadastrado, já formatado
                                            # Ex.: "12", "Maria", "F", "98763546" (sendo passados como string)

             sql = "INSERT INTO %s (%s) VALUES (%s)".format( table_fields[0], str_colum, str_value )

             cursor.execute(sql)
             conexao.commit()

# DELETA UM REGISTRO DA BASE DE DADOS
def Delete_reg (key_table, colum_value, delete_value):
     with conecta() as conexao:
         with conexao.cursor() as cursor:

            table_del_in = get_table_fields(key_table)[0]

            for colum in table_del_in[1]:
                if colum_value == colum:
                    del_colum = '\"%s\"'.format(colum)

            del_value = '\"%s\"'.format(delete_value)

            sql = "DELETE FROM %s WHERE %s = %s".format( table_del_in[0], del_colum, delete_value )
    
             cursor.execute(sql)
             conexao.commit()

 # ATUALIZA UM REGISTRO NA BASE DE DADOS
def update (key_table, new_value, cond_value):
     with conecta() as conexao:
         with conexao.cursor() as cursor:

             table_up_in = get_table_fields(key_table)[0]

             up_new = '\"%s\"'.format(new_value)

             up_conditional = '\"%s\"'.format(cond_value)

             sql = 'UPDATE %s SET %s WHERE %s'.format(table_up_in[0], up_new, up_conditional)

             cursor.execute(sql)
             conexao.commit()

# ESTE SELECIONA OS DADOS DA BASE DE DADOS
def select ( name_select, key_table, select_cond ):
    with conecta() as conexao:
        with conexao.cursor() as cursor:

            select_in_table = get_table_fields(key_table)[0]

            name_sel = '\"%s\"'.format(name_select)

            from_cond = '\"%s\"'.format(select_cond)

            sql = 'SELECT %s FROM %s FROM %s'.format(  name_sel ,select_in_table[1],  )

            cursor.execute(sql)
            resultado = cursor.fetchall()

            for linha in resultado:
                print(linha)