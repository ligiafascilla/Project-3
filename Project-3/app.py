# This is the main script.
from flask import Flask, jsonify, render_template

import pandas as pd
from sqlalchemy import create_engine

# Create database connection
connection_string= 'postgresql+psycopg2://postgres:1357@localhost:5432/Attacks_db'
engine = create_engine(connection_string)

app = Flask(__name__)

@app.route('/')
def main():
    # return '<h1>Hola Mundo</h1>'
    return render_template('index.html')

@app.route('/api')
def api():
    # Return the AVG of AGE for SEX
    response = pd.read_sql('select * from attacks', engine).groupby('Sex')['Age'].mean()
    response = {
        'labels': response.index.to_list(),
        'values': response.to_list(),
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=False)