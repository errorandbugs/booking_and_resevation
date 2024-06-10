from flask import Flask, Blueprint, render_template, request, redirect, send_file, url_for, flash
from model import db, User,Booking 
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from Form  import SigninForm,SignupForm,ResetRequestform,ResetPasswordForm
from flask_bcrypt import bcrypt,Bcrypt


reset_token_blueprint = Blueprint('reset_token' , __name__, url_prefix='/reset_token')

@reset_token_blueprint.route('/reset/<token>', methods=['GET' , 'POST'])



def reset_token(token, bcrypt):
    user=User.verify_token(token)
    if user is None:
        flash('that is invalid token or expired. Please try again.','warning')
        return redirect(url_for('reset_request'))

    form=ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        User.password=hashed_password
        db.session.commit
        flash('Password changed! you can now login','success')
        return redirect(url_for('signin'))
    return render_template('html', title= "Change password", form=form)