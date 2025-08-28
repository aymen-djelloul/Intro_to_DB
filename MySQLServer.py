import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""   # ضع كلمة السر إذا عندك
    )
    cur = conn.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")
except mysql.connector.Error as e:
    print("Error:", e)
finally:
    if conn.is_connected():
        cur.close()
        conn.close()
