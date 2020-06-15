import os
from settings import config
from flask import Flask


def init_app(environment="default"):
    app = Flask(__name__)
    app.config.from_object(config[environment])
    app.secret_key = os.urandom(16)
    os.environ['MONGODB_HOST'] = app.config['MONGODB_HOST']
    from models.articles.views import articles_blueprint
    app.register_blueprint(articles_blueprint)
    from models.crawler.views import spider_blueprint
    app.register_blueprint(spider_blueprint)

    return app
