import boto3
from botocore.exceptions import ClientError
from flask import Flask, jsonify, render_template
import json
import mysql.connector
import configparser
import os
print(os.getcwd())

app = Flask(__name__)

# Create a configparser object
config = configparser.ConfigParser()

# Read the properties file
config.read('properties.db')
print(f"Reading configuration file: {config.read('properties.db')}")

# Access the values from the 'database' section
user = config.get('database', 'user')
password = config.get('database', 'password')
host = config.get('database', 'host')
database = config.get('database', 'database')

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    return response

@app.route('/')
def index():
    # Establish the MySQL connection
    cnx = mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        database=database
    )

    cursor = cnx.cursor()

    # Create the table if it doesn't exist
    create_table_queries = [
        """
        CREATE TABLE IF NOT EXISTS studentlist (name VARCHAR(50) NOT NULL, roll INT NOT NULL, grade CHAR(1) NOT NULL);
        """,
        """
        CREATE TABLE IF NOT EXISTS employeelist (name VARCHAR(50) NOT NULL, employee_id INT NOT NULL, department VARCHAR(50) NOT NULL);
        """,
        """
        CREATE TABLE IF NOT EXISTS workerlist (name VARCHAR(50) NOT NULL, worker_id INT NOT NULL, job_title VARCHAR(50) NOT NULL);
        """,
        """
        CREATE TABLE IF NOT EXISTS salarylist (name VARCHAR(50) NOT NULL, roll_id INT NOT NULL, salary DECIMAL(10, 2) NOT NULL);
        """
    ]

    for query in create_table_queries:
        cursor.execute(query)

    # Commit the changes
    cnx.commit()

    # Insert values into the tables if they are empty
    cursor.execute("SELECT COUNT(*) FROM studentlist")
    count = cursor.fetchone()[0]

    if count == 0:
        insert_queries = [
            """
            INSERT INTO studentlist (name, roll, grade) VALUES (%s, %s, %s)
            """,
            """
            INSERT INTO employeelist (name, employee_id, department) VALUES (%s, %s, %s)
            """,
            """
            INSERT INTO workerlist (name, worker_id, job_title) VALUES (%s, %s, %s)
            """,
            """
            INSERT INTO salarylist (name, roll_id, salary) VALUES (%s, %s, %s)
            """
        ]

        values = [
            [('leo hank', 143, 'A'), ('jon rina', 124, 'B'), ('hylu sed', 564, 'C')],  # Example values for studentlist
            [('John Doe', 1001, 'HR'), ('Jane Smith', 1002, 'IT')],  # Example values for employeelist
            [('Mike Johnson', 2001, 'Engineer'), ('Sarah Anderson', 2002, 'Designer')],  # Example values for workerlist
            [('Mike Johnson', 2001, 5000.00), ('Jane Smith', 1002, 6000.00)]  # Example values for salarylist
        ]

        for i, query in enumerate(insert_queries):
            cursor.executemany(query, values[i])

        # Commit the changes
        cnx.commit()

        return "Tables created and values inserted successfully!"


    # # Retrieve data from the tables
    # select_queries = [
    #     "SELECT * FROM studentlist",
    #     "SELECT * FROM employeelist",
    #     "SELECT * FROM workerlist",
    #     "SELECT * FROM salarylist"
    # ]

    # tables = ['studentlist', 'employeelist', 'workerlist', 'salarylist']
    # data = {}

    # for i, query in enumerate(select_queries):
    #     cursor.execute(query)
    #     rows = cursor.fetchall()
    #     columns = [desc[0] for desc in cursor.description]
    #     table_data = []

    #     for row in rows:
    #         row_data = {}
    #         for j, value in enumerate(row):
    #             row_data[columns[j]] = value
    #         table_data.append(row_data)

    #     data[tables[i]] = table_data

    # # Close the database connection
    # cnx.close()

    # return jsonify(data)

@app.route('/employeelist')
def employeelist():
    # Establish the MySQL connection
    cnx = mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        database=database
    )

    cursor = cnx.cursor()

    # Retrieve data from the "employeelist" table
    select_query = "SELECT * FROM employeelist"
    cursor.execute(select_query)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    data = []

    for row in rows:
        row_data = {}
        for i, value in enumerate(row):
            row_data[columns[i]] = value
        data.append(row_data)

    # Close the database connection
    cnx.close()

    return jsonify({'employeelist': data})

@app.route('/workerlist')
def workerlist():
    # Establish the MySQL connection
    cnx = mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        database=database
    )

    cursor = cnx.cursor()

    # Retrieve data from the "workerlist" table
    select_query = "SELECT * FROM workerlist"
    cursor.execute(select_query)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    data = []

    for row in rows:
        row_data = {}
        for i, value in enumerate(row):
            row_data[columns[i]] = value
        data.append(row_data)

    # Close the database connection
    cnx.close()

    return jsonify({'workerlist': data})

@app.route('/salarylist')
def salarylist():
    # Establish the MySQL connection
    cnx = mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        database=database
    )

    cursor = cnx.cursor()

    # Retrieve data from the "salarylist" table
    select_query = "SELECT * FROM salarylist"
    cursor.execute(select_query)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    data = []

    for row in rows:
        row_data = {}
        for i, value in enumerate(row):
            row_data[columns[i]] = value
        data.append(row_data)

    # Close the database connection
    cnx.close()

    return jsonify({'salarylist': data})
@app.route('/studentlist')
def studentlist():
    # Establish the MySQL connection
    cnx = mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        database=database
    )

    cursor = cnx.cursor()

    # Retrieve data from the "studentlist" table
    select_query = "SELECT * FROM studentlist"
    cursor.execute(select_query)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    data = []

    for row in rows:
        row_data = {}
        for i, value in enumerate(row):
            row_data[columns[i]] = value
        data.append(row_data)

    # Close the database connection
    cnx.close()

    return jsonify({'studentlist': data})



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)