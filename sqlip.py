import mysql.connector

# Estabelecendo a conexão com o banco de dados
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='smartphone'
)

cursor = conn.cursor()

# cursor.execute('SELECT * FROM celulares')
# results = cursor.fetchall()
