import urllib.request,json
from .models import Source,Article

api_key = None
source_url = None
article_url = None
base_url =None
base_article_url = None

def configure_request(app):
    global api_key,source_url,article_url, base_article_url,base_url
    api_key = app.config['NEWS_API_KEY']
    source_url = app.config['NEWS_API_SOURCE_URL']
    # base_url = app.config ["NEWS_API_BASE_URL"]
    base_article_url = app.config["ARTICLES_API_BASE_URL"]


def getSources(category):

    getSourcesURL = source_url.format(category,api_key)
  
    with urllib.request.urlopen(getSourcesURL) as url:
        getSourcesData = url.read()
        getSourcesResponse = json.loads(getSourcesData)

        sourcesResults = None 

        if getSourcesResponse['sources']:
            sourcesResultsList = getSourcesResponse['sources']
            sourcesResults = processSources(sourcesResultsList)

    return sourcesResults        

def processSources(sourceLists):
    sourcesResults = []
    for sourceList in sourceLists:
        id = sourceList.get('id')
        name = sourceList.get('name')
        description = sourceList.get('description')
        url = sourceList.get('url')
        category = sourceList.get('category')
        language = sourceList.get('language')
        country = sourceList.get('country')

        sourceObject = Source(id,name,description,url,language,category,country)

        sourcesResults.append(sourceObject)

    return sourcesResults

def get_articles(id):
    """
    Function that gets the json Articles response to our url request
    """
    get_articles_url = base_article_url.format(id,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles_results(articles_results_list)

    return articles_results

def process_articles_results(articles_list):
    """
    Function  that processes the articles result and transform them to a list of Objects

    """
    
    articles_results = []
    for article_item in articles_list:
        id = article_item.get('id')
        title = article_item.get('name')
        author = article_item.get('author')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')

        if urlToImage:
            article_object = Articles(id, title, author, description, url, urlToImage, publishedAt, content)
            articles_results.append(article_object)

    return articles_results


def search_artciles(articles_name):
    
    search_articles_url = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey={}'.format(api_key,articles_name)
    with urllib.request.urlopen(search_articles_url) as url:
        search_articles_data = url.read()
        search_articles_response = json.loads(search_articles_data)

        search_articles_results = None

        if search_articles_response['results']:
            search_articles_list = search_articles_response['results']
            search_articles_results = process_articles_results(search_articles_list)


    return search_articles_results