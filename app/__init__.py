from flask import Flask
from config import configOptions

def create_app(config_name):
    app = Flask(__name__)

    #create app configuraions
    app.config.from_object(configOptions[config_name])

     # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

      # setting config
    from .requests import configRequest
    configRequest(app)


    return app 