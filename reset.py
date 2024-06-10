from flask import Flask, Blueprint, render_template, request, redirect, send_file, url_for, flash
from flask_mailman import Mail,EmailMessage
from reset_token_link import reset_token
from model import db, User,Booking
from signin import signin_blueprint
from signup import Signup_blueprint 
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from Form  import SigninForm,SignupForm,ResetRequestform
from flask_mailman import message

reset_blueprint = Blueprint('reset' , __name__, url_prefix='/reset')
@reset_blueprint.route('/', method=['GET' , 'POST'])


def send_mail(user):
    token=user.get_token()
    msg = message('Password Reset Request', recipients=[user.email], sender='basscee54@gmail.com')
    msg.body = f''' To = reset your password. please follow the link below.

{url_for('reset_token',token=token,_external=True)}

'''


def reset():
    if request.method == ['GET','POST'] :
        form = ResetRequestform()
        user = User.query.filter_by(email=form.email.date ).first()
        if user:
            send_mail()
            flash('Reset request sent. Check your mail.','success')
            return redirect(url_for('signup'))
        else :
            flash('unrecognised login details','error')
    return render_template('html for reset_password ', title='Reset requeust',form=form,)#legend="Reset_password#)


 