
import sqlite3
import pandas as pd

connection = sqlite3.connect('web.db')

df_data = pd.read_csv('bd_data.csv', index_col=0)
df_data.index.name = 'index_name'
df_data.to_sql('data',connection, index_label='index_name')

cursor = connection.cursor()

### Create
cursor.execute('CREATE TABLE products (product_id, product_name, price)')
connection.commit()

cursor.execute('CREATE TABLE products ([product_id] INTEGER PRIMARY KEY, [product_name] TEXT, [price] INTEGER)')

### Drop
cursor.execute('DROP TABLE products')
cursor.execute('DROP TABLE data')

### Insert
cursor.execute('''INSERT INTO products (product_id, product_name, price)
VALUES
(1, 'Computer', 800),
(2, 'Printer', 200),
(3, 'Tablet',300)
''')
connection.commit()

df_data2 = df_data.iloc[::-2]
df_data2.to_sql('data', connection, if_exists='append')

### Select
cursor.execute("SELECT * FROM data")
cursor.fetchone()
cursor.fetchall()

df = pd.DataFrame(cursor.fetchall())

cursor.execute("SELECT * FROM data WHERE A > 200")
df = pd.DataFrame(cursor.fetchall())

cursor.execute("SELECT * FROM data WHERE A > 200 AND B > 100")
df = pd.DataFrame(cursor.fetchall())

### Another reading
query = "SELECT * FROM data"
df = pd.read_sql(query, con=connection,index_col='index_name')


### Update & Delete
cursor.execute("UPDATE data SET A=218 WHERE index_name='b'")
connection.commit()

cursor.execute("UPDATE data SET A=220,B=228 WHERE index_name='b'")
connection.commit()

cursor.execute("DELETE FROM data WHERE index_name=1")
connection.commit()