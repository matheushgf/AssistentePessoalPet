import pymysql as mysql
import tkinter.messagebox as MessageBox

# Recebe dados e Insere no banco
def insert(nome_tabela, dados):
    campos = ', '.join(list(dados.keys()))
    valores = []
    for chave in dados:
        valores.append('"' + str(dados[chave]) + '"')
    valores = ', '.join(valores)
    mydb = mysql.connect(host='127.0.0.1', user='root', password='', db='mydb', charset='utf8mb4')
    cursor = mydb.cursor(mysql.cursors.DictCursor)
    cursor.execute('INSERT INTO {} ({}) VALUES ({})'.format(nome_tabela, campos, valores))
    cursor.execute("commit");
    MessageBox.showinfo("Status da ação", "Dados inseridos com sucesso");
    mydb.close()

def update(nome_tabela, dados):
    campos = ', '.join(list(dados.keys()))
    valores = []

    for chave in dados:
        valores.append('"' + str(dados[chave]) + '"')

    valores = ', '.join(valores)
    mydb = mysql.connect(host='127.0.0.1', user='petuser', password='', db='mydb', charset='utf8mb4')
    cursor = mydb.cursor(mysql.cursors.DictCursor)
    cursor.execute("UPDATE dono_pet SET endereço_dono=%s, telefone_dono=%s WHERE nome_dono=%s",(endereco, telefone, nome))
    cursor.execute("commit");
    MessageBox.showinfo("Status da ação", "Dados atualizados com sucesso");
    mydb.close()

def select(nome):
    mydb = mysql.connect(host='127.0.0.1', user='petuser', password='', db='mydb', charset='utf8mb4')
    cursor = mydb.cursor(mysql.cursors.DictCursor)
    resultado = cursor.execute("select telefone_dono from dono_pet WHERE nome_dono=%s",
                   nome)
    cursor.execute("commit");
    mydb.close()
    print(resultado)

#def delete