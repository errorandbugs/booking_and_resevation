#from flask import Blueprint, render_template,redirect,request
from captcha import ImageCaptcha
image =ImageCaptcha(width=280,height=100)

data=image.generate('hello156world')
image.write('hello156wordld,','demo.png')
