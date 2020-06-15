from flask import Blueprint, jsonify
from models.articles.article import Article

articles_blueprint = Blueprint('articles_blueprint', __name__)


@articles_blueprint.route('/articles/', methods=['GET'])
def getArticles():
    articles = Article.FetchAllArticles()
    return jsonify([article.json() for article in articles])


@articles_blueprint.route('/articles/<string:keyword>', methods=['GET'])
def SearchByKeyword(keyword):
    articles = Article.SearchByKeyword(keyword)
    return jsonify([article.json() for article in articles])

