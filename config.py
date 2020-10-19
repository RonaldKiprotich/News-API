import os

class Config:
    NEWS_API_SOURCE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    NEWS_API_ARTICLE = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'
    #NEWS_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    NEWS_API_KEY = '051cb299bf97459f902d123f95bde1c6'


class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}   