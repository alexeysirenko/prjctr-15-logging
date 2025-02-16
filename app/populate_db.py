import mysql.connector
import os

db_config = {
    "host": os.getenv("DATABASE_HOST", "localhost"),
    "user": os.getenv("DATABASE_USER", "testuser"),
    "password": os.getenv("DATABASE_PASSWORD", "testpassword"),
    "database": os.getenv("DATABASE_NAME", "testdb")
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

cursor.execute("""
DROP TABLE IF EXISTS users
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
)
""")

users = [("User{}".format(i), "user{}@example.com".format(i)) for i in range(1000000)]
cursor.executemany("INSERT INTO users (name, email) VALUES (%s, %s)", users)

conn.commit()
cursor.close()
conn.close()
print("Database populated successfully!")
