Backend Application:-
---------------------
Backend Python Flask Application
This repository contains the backend code for a Python Flask application. The application serves as the server-side component, handling requests and providing data to the frontend of the web application. It is built using the Flask framework, which is a lightweight and flexible web framework for Python.

Getting Started
To get started with this backend application, follow the instructions below:

Services Involved:
------------------
cloud : AWS
services:
1.EC2
2.IAM-----role with rds full access permission and attach to instance
3.RDS

Prerequisites
---------------
We are running this application on top of VM. So we need to launch an instance.
Create a mysql database in rds
Install all the dependencies which are mentioned in dependencies.sh file in this repo

Procedure
---------------
1. launch an instance

2. In RDS, create mysql database
Get the secrets like host,user,password
    allow 3306 from the instance sg
connect:
--------




1. connect to the instance 
   ssh command

mysql -h <rds endpoint> -u <username> -p 
this command will prompt you to enter the password

after connecting to the db run the following quesries to create tables and insert values in it

a. use <db name>;
b. CREATE TABLE <tableName>  (name VARCHAR(50) NOT NULL,roll INT NOT NULL, grade CHAR(1) 
NOT NULL );
c.show tables;
d.INSERT INTO <tableName> (name, roll, grade) VALUES ('leo hank', 103, 'A');
you can insert multiple values
e. select * from <tablename>;
    it will show the table with the values which you inserted


1. install the dependencies
   sh dependencies.sh

2. cofiguration:
   --------------
   open app.py and give the rds creds i.e. host,username,password,db name


3.  Run the application
    a.foreground------
    # python3 app.py
    b.background------
    # nohup python3 app.py &


app.py: This is the main application file where the Flask app is created and configured.
dependencies.sh: Contains a list of Python dependencies required by the application.

