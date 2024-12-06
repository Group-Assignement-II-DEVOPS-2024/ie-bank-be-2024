from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)

print(f"ENV: {os.getenv('ENV')}")
print(f"DBHOST: {os.getenv('DBHOST')}")
print(f"DBNAME: {os.getenv('DBNAME')}")
print(f"DBUSER: {os.getenv('DBUSER')}")

if os.getenv('ENV') == 'local':
    print("Running in local mode")
    app.config.from_object('config.LocalConfig')
elif os.getenv('ENV') == 'development':
    print("Running in development mode")
    app.config.from_object('config.DevelopmentConfig')
    print(f"Database URI after config: {app.config.get('SQLALCHEMY_DATABASE_URI')}")
elif os.getenv('ENV') == 'ghci':
    print("Running in github mode")
    app.config.from_object('config.GithubCIConfig')
elif os.getenv('ENV') == 'uat':
    print("Running in uat mode")
    app.config.from_object('config.UatConfig')
else:
    print(f"WARNING: Unknown environment: {os.getenv('ENV')}")

if not app.config.get('SQLALCHEMY_DATABASE_URI'):
    print("WARNING: SQLALCHEMY_DATABASE_URI not set, setting manually")
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DBUSER')}:{os.getenv('DBPASS')}@{os.getenv('DBHOST')}/{os.getenv('DBNAME')}"

print(f"Final Database URI: {app.config.get('SQLALCHEMY_DATABASE_URI')}")

db = SQLAlchemy(app)

from iebank_api.models import Account
if os.getenv('ENV') != 'ghci':
    with app.app_context():
        db.create_all()

CORS(app)

from iebank_api import routes
