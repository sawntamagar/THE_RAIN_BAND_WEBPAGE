import os

class Config:
   
   DEBUG = True
   SECRET_KEY = '1234567890'
   SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:9845721938@localhost/rain'
   SQLALCHEMY_COMMIT_ON_TEARDOWN = True
   FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
   FLASKY_MAIL_SENDER = 'Flasky Admin <sawntamagar36@gmail.com>'
   FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
   
   
   def init_app(app):
       pass
   





class DevelopmentConfig(Config):
    
    SECRET_KEY = '1234567890'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:9845721938@localhost/rain'
    DB_NAME = "sampl.db"
    DB_USERNAME = "postgres"
    DB_PASSWORD = "9845721938"
    DB_HOST = "localhost"
    DEBUG = True
    SQLALCHEMY_ECHO = True



class ProductionConfig(Config):
    
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:9845721938@localhost/rain'


class TestinConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:9845721938@localhost/rain'


config = {
    
    'development': DevelopmentConfig,
    'testing': TestinConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
    
}