import urllib.request,json
from .models import Source,Article

api_key = None
source_url = None
article_url = None

def configure_request(app):
    global api_key,source_url,article_url
    api_key = app.config['NEWS_API_KEY']
    source_url = app.config['NEWS_API_SOURCE_URL']
    article_url = app.config['NEWS_API_ARTICLE'] 


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

def getArticles():
    pass 
