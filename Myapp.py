from flask import Flask,render_template,flash,redirect,request, url_for
from flask_bcrypt import Bcrypt
from flask_mailman import Mail, EmailMessage
from model import db, User,Booking
from signin import signin_blueprint
from signup import Signup_blueprint
from signout import signout_blueprint
from feedback import feedback_blueprint
from reset_token_link import reset_token_blueprint
from model import db, User,Booking
from werkzeug.security import generate_password_hash, check_password_hash
from Form  import SigninForm,SignupForm,ResetRequestform,ResetPasswordForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:/// auth.db'
app.config['SECRET_KEY'] = 'yf24ey43487f'

app.config["STRIPE_PUBLIC_KEY"] = 'pk_test'
app.config['STRIPE_SECRET_KEY'] = 'sk_test'
#stripe.api_key = app.config['STRIPE_SECRET_KEY']


bcrypt = Bcrypt(app)
#admin = Admin(app)

def email_config():

    mail.init_app(app) 
    app.config['FLASK_ADMIN_SWATCH'] = 'Basscee'
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] ="basscee54@gmail.com"
    app.config['MAIL_PASSWORD']="^*%#(&^(TWYOT^(%@^&"
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True

mail =Mail(app)
    
db.init_app(app)
app.register_blueprint(signin_blueprint)
app.register_blueprint(Signup_blueprint)
app.register_blueprint(signout_blueprint)
app.register_blueprint(feedback_blueprint)
app.register_blueprint(reset_token_blueprint)
with app.app_context():
    db.create_all()


@app.route("/")
def Home():
    return render_template('index.html')

@app.route('/send_mail/<email>', methods=['GET','POST'])
def Send_Email(email ):
    msg_title  = "This Message was sent by the RESREVAR"
    sender = 'admin' 
    msg = EmailMessage(msg_title, sender=sender, recipients=[email])
    msg_body = "This the email body"
    data = {
        "App_name" : "Resrevar",
        "Body" : msg_body
    }

    msg.html = render_template('email.html',data=data)

    try: 
        mail.send(msg)
        return 'Email sent.... from '
    except Exception as e:
        print(e)
        return f"the email was not sent{e}"

'''
@app.route('/reset/<token>', methods=['GET','POST'])
def reset_token(token):
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
'''

if __name__ =="__main__" :
    app.run(debug = True)

    
