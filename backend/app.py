
import boto3
from botocore.exceptions import ClientError
from flask import Flask, jsonify
import json
import mysql.connector
import configparser

app = Flask(__name__)


@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    return response

@app.route('/')
def index():
    # Create a configparser object
    config = configparser.ConfigParser()

    # Read the properties file
    config.read('properties.db')

    # Access the values from the 'database' section
    user = config.get('database', 'user')
    password = config.get('database', 'password')
    host = config.get('database', 'host')
    database = config.get('database', 'database')

    # Establish the MySQL connection
    cnx = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            database=database
            )

    # Execute a query to retrieve data from the "employee" table
    cursor = cnx.cursor()
    query = "SELECT * FROM studentlist"
    cursor.execute(query)
    rows = cursor.fetchall()

    # Close the database connection
    cnx.close()


    return render_template('table.html', rows=rows)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
