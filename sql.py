import sqlite3
import pandas as pd



connection = sqlite3.connect('web.db')


df_data = pd.read_csv('bd_data.csv', index_col=0)
df_data.index.name = 'index_name'
df_data.to_sql('data',connection, index_label='index_name')


cursor = connection.cursor()

cursor.execute('CREATE TABLE products (product_id, product_name, price)')
connection.commit()

cursor.execute('DROP TABLE products')
cursor.execute('DROP TABLE data')


cursor.execute('CREATE TABLE products ([product_id] INTEGER PRIMARY KEY, [product_name] TEXT, [price] INTEGER)')