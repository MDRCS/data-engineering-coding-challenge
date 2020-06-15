from dotenv import load_dotenv

import os

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SSL_REDIRECT = False
    HOSTNAME = "0.0.0.0:5000"


class DevelopmentConfig(Config):
    DEBUG = True
    MONGODB_HOST = os.environ.get('MONGODB_HOST_DEV')


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    MONGODB_HOST = os.environ.get('MONGODB_HOST_TEST')
    WTF_CSRF_ENABLED = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,

    'default': DevelopmentConfig
}
