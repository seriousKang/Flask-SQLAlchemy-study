import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

db_file_path = os.path.abspath(os.getcwd() + "/../db") + "/test.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_file_path

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
