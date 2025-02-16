from flask import Flask, jsonify, request
import mysql.connector
import os

app = Flask(__name__)

db_config = {
    "host": os.getenv("DATABASE_HOST", "mysql"),
    "user": os.getenv("DATABASE_USER", "testuser"),
    "password": os.getenv("DATABASE_PASSWORD", "testpassword"),
    "database": os.getenv("DATABASE_NAME", "testdb")
}

@app.route('/slow', methods=['GET'])
def slow():
    timeout = request.args.get('timeout', default=2, type=int)
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    query = "SELECT SLEEP(%s);"
    cursor.execute(query, (timeout))
    conn.close()
    return jsonify({})

@app.route('/search', methods=['GET'])
def search_users():
    name = request.args.get('name', default="", type=str)

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM users WHERE name LIKE %s"
    cursor.execute(query, (name,))
    users = cursor.fetchall()
    conn.close()
    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
