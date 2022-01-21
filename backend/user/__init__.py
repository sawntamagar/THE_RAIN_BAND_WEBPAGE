from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_migrate import Migrate
 


db = SQLAlchemy()
migrate = Migrate()




def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    migrate.init_app(app, db)
    
    
    db.init_app(app)
   
  
    from .auth import auth as auth_blueprint
    from .views import views as views_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/')
    app.register_blueprint(views_blueprint, url_prefix='/')
    
    
   
    from .models import  User, Role
    
    
    create_database(app)


    return app



def create_database(app):
        db.create_all(app=app)
        print('Created Database!')
    
    

