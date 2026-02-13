import sqlite3
import pandas as pd
import time

conn = sqlite3.connect('sql_analytics.db')
cursor = conn.cursor()

with open("sql/create_tables.sql") as f:
    cursor.executescript(f.read())

with open("sql/insert_data.sql") as f:
    cursor.executescript(f.read())

query = "SELECT SUM(amount) as total_sales FROM sales"
start = time.time()
cursor.execute(query)
result = cursor.fetchall()
end = time.time()

print("Total Sales:", result[0][0])
print("Execution Time:", end - start, "seconds")

conn.close()
import sqlite3
import pandas as pd
import time

conn = sqlite3.connect('sql_analytics.db')
cursor = conn.cursor()

with open("sql/create_tables.sql") as f:
    cursor.executescript(f.read())

with open("sql/insert_data.sql") as f:
    cursor.executescript(f.read())

query = "SELECT SUM(amount) as total_sales FROM sales"
start = time.time()
cursor.execute(query)
result = cursor.fetchall()
end = time.time()

print("Total Sales:", result[0][0])
print("Execution Time:", end - start, "seconds")

conn.close()
