from flask import Blueprint, request, jsonify
from models.crawler.spider import Spider

spider_blueprint = Blueprint('spider_blueprint', __name__)


@spider_blueprint.route('/crawler/articles/<string:link>', methods=['GET', 'POST'])
def LoadArticles(link):
    """
    URL EXAMPLE
    :param link: -> http://127.0.0.1:5000/crawler/articles/bbc.com
    :return:
    """
    link = "https://" + link
    spider = Spider(link)
    articles_urls = spider.crawl_articles_urls()
    articles = spider.crawl_articles(articles_urls)
    if request.method == 'POST':
        spider.bucket_store(articles)

    return jsonify([article.json() for article in articles])


@spider_blueprint.route('/crawler/article/<string:article_url>', methods=['GET', 'POST'])
def LoadOneArticle(article_url):
    """
    URL EXAMPLE
    :param article_url: -> http://127.0.0.1:5000/crawler/article/world-africa-53040513
    :return:
    """

    article_url = "https://www.bbc.com/news/" + article_url
    article = Spider.crawl_article(article_url)
    if request.method == 'POST':
        article.save_database()

    return jsonify(article.json())
