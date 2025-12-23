import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM main_product;")
count = cursor.fetchone()[0]
print(f"Number of products: {count}")
if count > 0:
    cursor.execute("SELECT name FROM main_product;")
    products = [row[0] for row in cursor.fetchall()]
    print("Products:", products)
conn.close()