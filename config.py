import os

class Config:

NEWS_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'


NEWS_API_KEY = os.environ.get('MOVIE_API_KEY')


class Prodconfig(Config):
    pass