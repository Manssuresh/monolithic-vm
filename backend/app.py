from flask import Flask, render_template
import mysql.connector
import os

app = Flask(__name__)

# To allow requests from all origins
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS, HEAD, GET, POST'
    return response

@app.route('/')
def index():
    db_host = os.environ.get('DB_HOST')
    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')
    db_name = os.environ.get('DB_NAME')
    table_name = os.environ.get('TABLE_NAME')

    cnx = mysql.connector.connect(user=db_user, password=db_password,
                                   host=db_host, database=db_name)
    cursor = cnx.cursor()
    query = "SELECT * FROM {}".format(table_name)
    cursor.execute(query)
    rows = cursor.fetchall()
    cnx.close()

    return render_template('table.html', rows=rows)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
