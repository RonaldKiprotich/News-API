from flask import render_template,request,redirect,url_for
from ..requests import getSources
from ..models import Source
from . import main

@main.route('/')
def index():
    
    news = getSources()

    title = 'Home, News Highlights'

    return render_template('index.html',title = title, news = news) 



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
