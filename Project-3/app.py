import json
from flask import Flask, jsonify, render_template, request
from sqlalchemy import create_engine

# Create database connection
connection_string = 'postgresql+psycopg2://postgres:1357@localhost:5432/Attacks_db'
engine = create_engine(connection_string)

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/api/years')
def get_years():
    query = "SELECT DISTINCT year FROM attacks"
    result = engine.execute(query)
    years = [row[0] for row in result]
    return jsonify(years)

@app.route('/api/activities')
def get_activities():
    query = "SELECT DISTINCT activity FROM attacks"
    result = engine.execute(query)
    activities = [row[0] for row in result]
    return jsonify(activities)

@app.route('/api/filter')
def filter_data():
    year = request.args.get('year')
    activity = request.args.get('activity')

    query = "SELECT * FROM shark_attacks WHERE year = %s AND activity = %s"
    result = engine.execute(query, (year, activity))
    data = [dict(row) for row in result]

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=False)
