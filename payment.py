from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash
import requests as request
from model import User, Items, db

payment_blueprint = Blueprint ('payments', __name__, url_prefix='/payment')
@payment_blueprint.route('/', methods = ['POST'])

def initiate_payment():
    amount = request.form ['amount']
    email = request.form ['email']
    paystack_secret_key = ['123456']
    payload = {'amount': amount * 100,
              'email' : email,
              'currency' : 'NGN' ,
              'callback_url' : url_for ('payment.payment_callback' , eternal = True), 
              'metadata': {'custom_field': [{'item_id': Items.id , 
                                             'item_name': Items.name  
                                              }]
                                             }     
                }

    headers = {'Content type' : 'Applicatiom/json' , 'authorization' : f'bearer (paystack_secret_key)'
            } 
    response = request.post  ("https://api.paystack.co/tansaction/initialize" , headers = headers , json=payload)
    if   response.status_code == 200:
        data = response.json()
        return redirect (['data'] , ['authorization_url'])
    
    
    else:
        flash('Retry' , 'Error')
        return render_template('home')


payment_callback_blueprint = Blueprint ('payments', __name__, url_prefix='/payment_callback')
@payment_callback_blueprint.route('/')
def payment_callback():
    transaction_reference = request.arg.get('reference')
    paystack_secret_key = ""

    headers = {'content type' : 'Applicatiom/json'} 

response = request.post("https://api.paystack.co/tansaction/initialize" , headers = headers , json= payload) # type: ignore
if response.status_code == 200:
    data = response.json()
    if data ['data']['status'] == 'success':
        flash ('payment successful')

    else:
        flash('payment unsuccessful')

