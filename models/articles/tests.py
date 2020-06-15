import unittest
import os
from utils.database import Database
from app import init_app as init_app_test


class ArticleTest(unittest.TestCase):

    def init_app(self):
        return init_app_test(
            'testing'
        )

    def setUp(self) -> None:
        self.app_factory = self.init_app()
        self.db_name = os.environ['MONGODB_HOST']
        self.app = self.app_factory.test_client()

    def test_getArticles(self):
        """
            Fetch articles Test
        """
        rv = self.app.get("/articles/")
        assert "[200 OK]" in str(rv)

    def test_SearchByKeyword(self):
        """
            Search By Keyword Test
        """
        rv = self.app.get("/articles/coronavirus")
        assert "[200 OK]" in str(rv)
