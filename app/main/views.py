from flask import render_template,request,redirect,url_for
from ..requests import getSources
from ..models import Source
from . import main

@main.route('/')
def index():

    business = getSources('business')

    title = 'Home, News Highlights'

    return render_template('index.html',title = title, business = business) 
