from datetime import date
from flask import Flask,redirect,render_template,request,Blueprint
from model import db,User,Items
from Form import BookingForm,SigninForm,SignoutForm,SignupForm
from flask_login import login_required

booking_blueprint = Blueprint('booking',__name__)

@booking_blueprint.route('/book',methods=['GET','POST'])
@login_required
def book_room():

    form = BookingForm()
    if form.validate_on_submit():
        room_id = form.room_id.data
        data = form.date.data
        user_id =form.user_id.data

        Room = Room.query.get(room_id)
        booking = booking(room = Room,date = date, user_id = user_id  )
        db.session.add(booking)
        db.commit()
        return 'Booking successfull'
    return render_template('booking.html', form=form)


def find_by_id(cls, id):
    booking = cls.query.filter_by(id=id)
    return booking

def data(self):
    return {
    "date_of_arrival": self.date_of_arrival,
    "date_of_departure": self.date_of_departure,
    "status": self.status,
    "room_id": self.room_id,
    "user_id": self.user_id,
    }

    
  
    
def get_all(cls):
    bookings = cls.query.all()
    return bookings