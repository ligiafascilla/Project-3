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
    query = 'SELECT DISTINCT "Year" FROM attacks'
    result = engine.execute(query)
    years = [row[0] for row in result]
    return jsonify(years)

@app.route('/api/countries')
def get_countries():
    query = 'SELECT DISTINCT "Country" FROM attacks'
    result = engine.execute(query)
    countries = [row[0] for row in result]
    return jsonify(countries)

@app.route('/api/types')
def get_types():
    query = 'SELECT DISTINCT "Type" FROM attacks'
    result = engine.execute(query)
    types = [row[0] for row in result]
    return jsonify(types)

@app.route('/api/filter')
def filter_data():
    year = request.args.get('Year')
    country = request.args.get('Country')
    type = request.args.get('Type')

    query = 'SELECT * FROM attacks WHERE "Year" = %s AND "Country" = %s AND "Type" = %s'
    result = engine.execute(query, (year, country, type))
    data = [dict(row) for row in result]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=False)
