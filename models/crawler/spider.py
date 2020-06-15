import re

import requests
from bs4 import BeautifulSoup
from models.articles.article import Article
from models.crawler.patterns import RegexPattern


class Spider(object):

    def __init__(self, base):
        self.base = base

    def __repr__(self):
        return f"base url : {self.base}"

    def crawl_articles_urls(self):
        content = requests.get(self.base).content
        soup = BeautifulSoup(content, 'html.parser')
        links = soup.find_all('a')

        links = set(link.get('href') for link in links)

        articles_urls = []

        for link in links:
            path = re.match(RegexPattern.path_pattern, link)
            if path is not None:
                article = re.findall(RegexPattern.article_pattern, path.group(0))
                if any(article):
                    articles_urls.append(self.base + path.group(0))

        return articles_urls

    @staticmethod
    def crawl_articles(articles_urls):
        articles = []
        for article_url in articles_urls:
            article = Spider.crawl_article(article_url)
            if article is not None:
                articles.append(article)

        return articles

    @staticmethod
    def crawl_article(article_url):
        article = Article(url=article_url)
        article.load_article()
        if article.title == "":
            return None
        return article

    @staticmethod
    def bucket_store(articles):
        for article in articles:
            article.save_database()

