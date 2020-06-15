import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest

from models.articles.tests import ArticleTest
from models.crawler.tests import SpiderTest

if __name__ == "__main__":
    unittest.main()
