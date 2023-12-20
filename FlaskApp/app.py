import sqlite3
from flask import Flask, request, jsonify


app = Flask(__name__)

# Initialize the database (for demo purposes)
def init_db():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,
              name TEXT, age INTEGER)''')
    c.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
    c.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")

    # lisää uusia henkilöitä tähän

    conn.commit()
    conn.close()

init_db()



# Route to query users by name
@app.route('/users')
def get_users():
    name = request.args.get('name')

    query = f"SELECT * FROM users WHERE name = '{name}'"

    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute(query)
    users = cursor.fetchall()
    conn.close()

    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
