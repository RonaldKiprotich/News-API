import urllib.request,json
from .models import Source,Article

api_key = None
source_url = None
article_url = None

def configRequest(app):
    global api_key,source_url,article_url
    api_key = app.config['NEWS_API_KEY']
    source_url = app.config['NEWS_API_SOURCE_URL']
    article_url = app.config['NEWS_API_ARTICLE'] 
