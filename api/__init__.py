from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from.models import db
from flask_restx import Api,Resource,Namespace
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


CORS(app)

db.init_app(app)


migrate = Migrate(app,db)
ma = Marshmallow(app)
api = Api(app)

from api import models, routes

