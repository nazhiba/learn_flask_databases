from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

def create_app():
     app = Flask(__name__, template_folder='template')
     app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./testdb.db"
     
     # NEW
     app.secret_key = "SOME KEYS"
     db.init_app(app)

     login_manager = LoginManager()
     login_manager.init_app(app)

     from models import User
     @login_manager.user_loader
     def user_loader(id):
          return User.query.get(id)

     bcrypt = Bcrypt(app)

     # Import nanti
     from routes import register_routes
     register_routes(app, db, bcrypt)

     migrate = Migrate(app,db)
     return app