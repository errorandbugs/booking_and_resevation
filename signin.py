from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user
from Form import SigninForm
from model import db, User,Booking

signin_blueprint = Blueprint('signin' , __name__, url_prefix='/signin')

@signin_blueprint.route('/', methods=['GET' , 'POST'])
def signin():
    form = SigninForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('market_page'))
        else:
            flash('Username and password are not match! Please try again', category='danger')

    return render_template('signin.html', form=form)
