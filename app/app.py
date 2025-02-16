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
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    query = "SELECT SLEEP(3);"
    cursor.execute(query)
    conn.close()
    return jsonify({})

@app.route('/users', methods=['GET'])
def get_users():
    offset = request.args.get('offset', default=0, type=int)
    limit = request.args.get('limit', default=10, type=int)

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM users LIMIT %s OFFSET %s"
    cursor.execute(query, (limit, offset))
    users = cursor.fetchall()
    conn.close()
    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
