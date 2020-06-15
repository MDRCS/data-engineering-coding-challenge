import unittest
import os
from app import init_app as init_app_test
from utils.database import Database
import models.articles.constants as ArticleConstants


class SpiderTest(unittest.TestCase):

    def init_app(self):
        return init_app_test(
            'testing'
        )

    def setUp(self) -> None:
        self.app_factory = self.init_app()
        self.db_name = os.environ['MONGODB_HOST']
        self.app = self.app_factory.test_client()

    def tearDown(self) -> None:
        Database.delete_many(ArticleConstants.Collection, {})

    def test_LoadArticles(self):
        """
            Fetch articles Test
        """
        post_response = self.app.post("/crawler/articles/bbc.com")
        assert "[200 OK]" in str(post_response)

        get_response = self.app.get("/crawler/articles/bbc.com")
        assert str(get_response) == str(post_response)

    def test_LoadOneArticle(self):
        """
            Search By Keyword Test
        """
        post_response = self.app.post("/crawler/article/world-africa-53040513")
        assert "[200 OK]" in str(post_response)

        get_response = self.app.get("/crawler/article/world-africa-53040513")
        assert str(get_response) == str(post_response)


