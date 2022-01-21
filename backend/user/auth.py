from flask import Blueprint, request
from flask import jsonify, session
from flask_login import login_required, login_user, logout_user
from user.models import User, Role
from werkzeug.security import check_password_hash, generate_password_hash
import validators
import psycopg2
import psycopg2.extras
from user import db
from constant import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_409_CONFLICT





DB_NAME = "sampl.db"
DB_USERNAME = "postgres"
DB_PASSWORD = "9845721938"
DB_HOST = "localhost"



auth = Blueprint('auth', __name__)


conn = psycopg2.connect(dbname=DB_NAME, user=DB_USERNAME, password=DB_PASSWORD, host=DB_HOST)

@auth.route('/')
def home():
    return ('This is home page')



@auth.route('/register', methods = ['POST'])      
def register():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    
   
    
    if len(password) < 6:
        return jsonify({'error': "password is to short"}),
        HTTP_404_BAD_REQUEST
        
   
    if len(username) < 6:
        return jsonify({'error': "username is to short"})
        HTTP_404_BAD_REQUEST
        
   
    if not username.isalnum() or " " in username:
        return jsonify({'error': "username should be alphanumeric and also no space"}),
        HTTP_404_BAD_REQUEST
        
    if not validators.email(email):
            return jsonify({'error': "email isnot valid"})
            HTTP_404_BAD_REQUEST
        
    if User.query.filter_by(email=email).first() is not None:  
        return jsonify({'error': "email is taken"})
        HTTP_409_CONFLICT
    
    if User.query.filter_by(username=username).first() is not None:  
        return jsonify({'error': "username is taken"})
        HTTP_409_CONFLICT    
        
    password = generate_password_hash(password)
    user = User(username=username, email=email, password=password)    
        
   
    db.session.add(user)
    db.session.commit()
    
    return jsonify(
        {
            'message': "user created",
            'user': {
                'username':username, 'email':email
            }
            
        }
    ),HTTP_201_CREATED
                        
  
        

@auth.route('/login', methods = ['POST'])
def login():
    
    username = request.json['username']
    password = request.json['password']
    
    if username and password:
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        
        sql = "SELECT * FROM public.users WHERE username=%s"
    
        sql_where = (username,)
        
        cursor.execute(sql, sql_where)
        row = cursor.fetchone()
        username = row['username']
        password = row['password']
        if row:
            check_password_hash(password, password)
            session['username'] = username
            cursor.close()
            return jsonify({'message': "you have logged in successfully"})
        else:
            resp = jsonify({'Bad Request': "invalid password"})
            resp.status_code = 400
            
        
    else:
        resp: jsonify({'message': "Bad Request - invalid credentials"})  
        resp.status_code = 400
        return resp  
        



@auth.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username', None)
        return jsonify({'message': "you have successfully logout"})
    
    

