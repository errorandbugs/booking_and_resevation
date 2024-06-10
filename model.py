from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import secrets
from datetime import datetime
from itsdangerous import TimedSerializer as serializer


db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(length=100) , unique = True , nullable = False)
    lastname = db.Column(db.String(length=100) , unique = False , nullable = False)
    email = db.Column(db.String(length=100) , unique = True , nullable = False)
    password = db.Column(db.String(20,) , nullable = False)
    phonenumber = db.Column(db.Integer, unique = True , nullable = False)
    items = db.relationship('Items', backref = 'owned_user', lazy=True)


    def set_pass(self, password):
        self.password = generate_password_hash(password)

    def check_pass(self, password):
        return check_password_hash(self.password, password)

    def generate_reset_token(self,expires_sec=1200):
        serial=serializer(app.config['SECRET_KEY'], expires_in=expires_sec)
        return serial.dumps({'user.id':self.id}).decode('utf-8')
        #self.reset_token = secrets.token_urlsafe(32)
        #self.reset_token = datetime.datetime.now()+datetime.timedelta(hours=1)
    
    @staticmethod
    def verify_token(token):
        serial=serializer(app.config['SECRET_KEY'])
        try:
            serial.load(token)['user_id']
        except:
            return None
        return User.query.get()
class Items(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(100) , unique = True , nullable = False)  
    price = db.Column(db.Integer(),nullable=False)
    desc = db.Column(db.String(length=1024),nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),unique=True)
    room_number =db.Column(db.String(100),unique=True)
    capacity = db.Column(db.Integer)

class Ride(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),unique=True)
    ride_number=db.Column(db.String(100),unique=True)
    colour = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Room{self.room_number}"
    

class Booking(db.Model):
  #  __tablename__ = "booking"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_of_arrival = db.Column(db.Date, nullable=False)
    date_of_departure = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), default="pending")
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    room = db.relationship('Room', backref=db.backref('bookings', lazy=True))
    ride_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    u_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    ride = db.relationship('Ride', backref=db.backref('booking', lazy=True))
    
    
        
   

    def __repr__(self):
        return f"Items(name={self.name},desc={self.desc})"
