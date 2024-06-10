from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash,session
from flask_login import logout_user
from model import db, User,Booking
from signin import signin_blueprint
from signup import Signup_blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy


signout_blueprint = Blueprint('signout' , __name__, url_prefix='/signout')

@signout_blueprint.route('/', methods=['GET' , 'POST'])
def signout():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("login"))

def send_mail():
    pass