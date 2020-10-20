from flask import render_template,request,redirect,url_for
from ..requests import getSources, get_articles
from ..models import Source
from . import main

@main.route('/')
def index():
    
    news = getSources()

    title = 'News Highlights'

    return render_template('index.html',title = title, news = news) 

@main.route('/general/')
def general():
    
    generals = get_articles("general")

    title = 'General Articles'

    return render_template('general.html',title = title, generals = generals) 

@main.route('/entertainment/')
def entertainment():
    
    entertainment = get_articles("entertainment")

    title = 'Entertainment News.'

    return render_template('entertainment.html',title = title, entertainment = entertainment) 

@main.route('/sports/')
def sports():
    
    sports = get_articles("sports")

    title = 'Sports News.'

    return render_template('sports.html',title = title, sports = sports) 


@main.route('/newsarticle/<id>')
def newsarticle(id):

    """
    Function that returns the article details page and its data
    """
    articles_items = get_articles(id)
    title = f'{id} | News Articles'
    return render_template('newsarticle.html',title = title,articles = articles_items)


