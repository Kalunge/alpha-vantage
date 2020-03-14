from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from configs.config import Development
import psycopg2

myapp = Flask(__name__)
myapp.config.from_object(Development)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@127.0.0.1:5432/forex'


db = SQLAlchemy(myapp)


from models.Forex import Forexx


conn = psycopg2.connect("dbname='forex' user='postgres' host='localhost' password='123456'")
cur = conn.cursor()

@myapp.cli.command('db_create')
def create_db():
    db.create_all()
    print('Database Created')

@myapp.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Database dropped')

@myapp.cli.command('db_seed')
def db_seed():
    pass


myapp.run(debug=True)
