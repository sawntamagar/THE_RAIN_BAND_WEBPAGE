
from werkzeug.security import generate_password_hash, check_password_hash
from user import db
from flask_login import UserMixin





class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')
    username = db.Column(db.String(255),index=True, unique = True )
    email = db.Column(db.String(255), index=True, unique = True)
    password = db.Column(db.String(255))
    roles = db.relationship('Role', backref="users")
   
 
    # role = db.relationship('Role', backref='role')
   
   
    def __init__(self, username, email, password):
        
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        


    def password_is_valid(self, password):
       
        return check_password_hash(self.password, password)


    def save(self):
        
        db.session.add(self)
        db.session.commit()


    
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    # users = db.relationship('User', backref='role')
   
    # role_id = db.Column(db.Integer, db.ForeignKey('users.id'))
 
        
        
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
     
    def update():
        return session_commit()
    
    def delete(self, role):
        db.session.delete(role)
        return session_commit()
        
    def save(self):
        
        db.session.add(self)
        db.session.commit()

    
            
