from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user
from model import db, User,Booking
from Form import SignupForm
Signup_blueprint = Blueprint('signup' , __name__, url_prefix='/signup')

@Signup_blueprint.route('/', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f"Account created successfully! You are now logged in as {user_to_create.username}", category='success')
        return redirect(url_for('market_page'))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('signup.html', form=form)
