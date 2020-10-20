from flask import render_template,request,redirect,url_for
from ..requests import getSources, get_articles
from ..models import Source
from . import main

@main.route('/')
def index():
    
    news = getSources()

    title = 'Home, News Highlights'

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


@main.route('/newsarticle/<id>')
def newsarticle(id):

    """
    Function that returns the article details page and its data
    """
    articles_items = get_articles(id)
    title = f'{id} | News Articles'
    return render_template('newsarticle.html',title = title,articles = articles_items)

@main.route('/search/<articles_name>')
def search(articles_name):
    articles_name_list = articles_name.split(" ")
    articles_name_format = "+".join(articles_name_list)
    searched_articles = searched_articles(articles_name_format)
    title = 'News results'
    search_articles = request.args.get('articles_search')
    if search_articles:
        return redirect(url_for('main.search',articles_feed=search_articles))
    else:
        return render_template('search.html',related=search_articles,title=title)
