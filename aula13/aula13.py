import pymysql
print(pymysql.version_info)

#Cria a conexão com o banco de dados
conexao = pymysql.connect(
    host="localhost",  #endereço do servidor (local = "localhost")
    user="seu_usuario",    #usuario do MySQL
    password="",  #senha do MySQL
    database=" bd_livrariaonline", #banco que você ja criou 
    port=3306                 #porta padrão do MySQL(opcional)
)


#Cria o cursor - versão dicionario (retorna {"coluna":valor})
cursor=conexao.cursor(pySQL.cursors.DictCursor)


#Buscar todos os registros

cursor.execute("SELECT * FROM Clientes")
todos = cursor.fetchall()
print(todos)


for cliente in todos:
    print(cliente["nome"], cliente["email"], "-",cliente
    ["telefone"])