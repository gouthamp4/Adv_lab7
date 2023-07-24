from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import DateTime
from datetime import datetime
from flask_bcrypt import Bcrypt

app = Flask(__name__,
            static_url_path='',
            static_folder='static', template_folder='viewtemplates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config["SECRET_KEY"] = "2T83MIP9CX-5M0RHEL472-PUX0OQDCAT"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
sqlDb = SQLAlchemy(app)
pwdHasher = Bcrypt(app)


class Customer(sqlDb.Model):
    customer_id = sqlDb.Column(sqlDb.Integer, primary_key=True)
    first_name = sqlDb.Column(sqlDb.String(80),nullable=False)
    last_name = sqlDb.Column(sqlDb.String(120),nullable=False)
    email_addr = sqlDb.Column(sqlDb.String(120),unique=True, nullable=False)
    passcode = sqlDb.Column(sqlDb.String(10),nullable=False)
    created_at = sqlDb.Column(DateTime, default=datetime.now)

with app.app_context():
    sqlDb.create_all()