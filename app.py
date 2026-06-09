import sqlite3
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def w209():
    file = 'about9.jpg'
    return render_template('w209.html', file=file)

@app.route('/status')
def api_demo():
    return render_template('api-demo.html')

# ── STEP 2: /api — returns {"x": 5} ──────────────────────────────
@app.route('/api')
def api():
    return jsonify({"x": 5})

# ── STEP 3: /players/count - total rows in Users table ───────────
@app.route('/players/count')
def players_count():
    conn = sqlite3.connect('players_20.db')
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM Users")
    count = cur.fetchone()[0]
    conn.close()
    return jsonify({"count": count})

# ── STEP 4: /players/get_nationality — lookup by short_name ──────
@app.route('/players/get_nationality')
def get_nationality():
    player = request.args.get('player', '')
    conn = sqlite3.connect('players_20.db')
    cur = conn.cursor()
    cur.execute("SELECT nationality FROM Users WHERE short_name = ?", (player,))
    row = cur.fetchone()
    conn.close()
    if row:
        return jsonify({"nationality": row[0]})
    return jsonify({"error": "Player not found"}), 404

if __name__ == '__main__':
    app.run()
