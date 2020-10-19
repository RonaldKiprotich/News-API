import os

class Config:
    NEWS_API_SOURCE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    NEWS_API_ARTICLE = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'
    ARTICLES_API_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey=fdee0f42def74c7bad48a87e16fd6f08'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')


class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}   