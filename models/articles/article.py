import uuid

import requests
from bs4 import BeautifulSoup



class Article(object):

    def __init__(self, url, title="", text="", tags=[], publish_date=None, author="", _id=None):
        self.title = title
        self.text = text
        self.link = url
        self.tags = tags
        self.publish_date = publish_date
        self.author = author
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return f"{self.title} - {self.author} - {self.publish_date} \n {self.text} \n {self.tags}"

    def load_article(self):
        page = requests.get(self.link).content
        soup = BeautifulSoup(page, 'html.parser')

        title = Article.load_title(soup)
        if title is None or title.text == "":
            return

        self.title = title.text
        self.text = Article.load_body(soup)
        self.publish_date = Article.load_date(soup)
        self.author = Article.load_author(soup)
        self.tags = Article.load_tags(soup)

    @staticmethod
    def load_title(soup):
        return soup.find("h1", {"class": "story-body__h1"})

    @staticmethod
    def load_body(soup):
        paragraphs = soup.find_all('p')
        body = ""
        for p in paragraphs[12:]:
            body += p.text
        return body

    @staticmethod
    def load_tags(soup):
        tags = []
        for div in soup.findAll('li', attrs={'class': 'tags-list__tags'}):
            tags.append(div.find('a').text)
        return tags

    @staticmethod
    def load_author(soup):
        author = soup.find("span", {"class": "byline__name"})
        if author is not None:
            return author.text[3:]
        return ""

    def json(self):
        return {
            "url": self.link,
            "publish_date": self.publish_date,
            "author": self.author,
            "title": self.title,
            "text": self.text,
            "tags": self.tags,
            "_id": self._id,
        }

