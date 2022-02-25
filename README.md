# FMS-RESTAPI-1 (Python, Flask, Flask-SQLAlchemy and MySQL)

_FMS-RESTAPI-1 is a REST API for create, read, update and delete (CRUD) notes._ 

## Quick Start

### Prerequisites

1. Python
2. MySQL

### Installation
1. Create your virtual environment
``` 
py -m venv your_environment
```
2. Activate your virtual environment
3. Install pip modules 
``` 
pip install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy pymysql
```
4. MySQL: create new database "your_mysql_db" and create a table "note" with 3 columns:

- ID (INT, PRIMARY KEY, AUTOINCREMENT)
- title (VARCHAR 30)
- content (VARCHAR 100)

5. start flask server
``` 
py src/app.py
```