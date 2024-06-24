import mysql.connector
from mysql.connector import Error

# Configuração da conexão
config = {
    'user': 'root',
    'password': '',  # Substitua pelo seu password
    'host': '127.0.0.1',
    'raise_on_warnings': True
}

try:
    # Conectando ao servidor MySQL
    conn = mysql.connector.connect(**config)
    if conn.is_connected():
        print("Conectado ao servidor MySQL")

    cursor = conn.cursor()

    # Listar todos os bancos de dados
    cursor.execute("SHOW DATABASES")
    databases = cursor.fetchall()
    print("Databases available:")
    for db in databases:
        print(db[0])

    # Selecione o banco de dados correto
    database_name = 'loja' 

    if (database_name,) in databases:
        conn.database = database_name
        print(f"Usando o banco de dados '{database_name}'")
    else:
        print(f"Database '{database_name}' não encontrado. Por favor, verifique o nome do banco de dados.")
        cursor.close()
        conn.close()
        exit()

    # Função para ler dados de uma tabela
    def read_table(table_name):
        try:
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except Error as e:
            print(f"Erro ao ler a tabela {table_name}: {e}")

    # Lendo dados das tabelas
    print("Clientes:")
    read_table('cliente')

    print("\nPedidos:")
    read_table('pedidos')

except Error as e:
    print(f"Erro ao conectar ao MySQL: {e}")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Conexão ao MySQL encerrada")