from flask import Flask, render_template, jsonify, request
import json
import os
import mysql.connector
from mysql.connector import Error

app = Flask(__name__, template_folder='templates', static_folder='static')

def load_metadata():
    """Charge les métadonnées depuis le fichier JSON dans deploy"""
    metadata_path = os.path.join(os.path.dirname(__file__), '..', 'deploy', 'metadata.json')
    try:
        with open(metadata_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "site": {"name": "CyberCTF Library", "description": "A Capture The Flag platform"},
            "navigation": {"main": [], "auth": []},
            "footer": {"links": [], "social": []},
            "challenge": {"title": "Challenge", "description": "Description", "skills": [], "points": 0},
            "cta": {"label": "Start", "link": "/"}
        }

# MySQL connection utility
def get_db_connection():
    return mysql.connector.connect(
        host='db',
        user='acmeuser',
        password='acmepass',
        database='acme_store',
        port=3306
    )

@app.route('/')
def home():
    metadata = load_metadata()
    return render_template('home.html', metadata=metadata)

@app.route('/api/metadata')
def api_metadata():
    return jsonify(load_metadata())

@app.route('/books')
def books():
    metadata = load_metadata()
    return render_template('books.html', metadata=metadata)

@app.route('/search')
def search():
    q = request.args.get('q', '')
    found = False
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        # Vulnerable SQL: direct string interpolation
        sql = f"SELECT * FROM books WHERE title LIKE '%{q}%'"
        cursor.execute(sql)
        result = cursor.fetchone()
        found = result is not None
    except Error:
        # Suppress errors for blind SQLi
        pass
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass
    return render_template('search_result.html', found=found, q=q)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 