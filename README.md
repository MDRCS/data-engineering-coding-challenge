[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

### + Data engineering Coding Challenge

    + Data engineering Coding Challenge

    % Challenge - News Content Collect and Store
    The goal of this coding challenge is to create a solution that crawls for articles from a news website, cleanses the response,
    stores it in a mongo database, then makes it available to search via an API.

    %% Specifications %%

    - Write an application to crawl articles on a news website such as theguardian.com or bbc.com using a crawler framework such as Scrapy. You can use a crawl framework of your choice and build the application in Python.
    - The application should cleanse the articles to obtain only information relevant to the news story, e.g. article text, author, headline, article url, etc. Use a framework such as Readability to cleanse the page of superfluous content such as advertising and HTML.
    - Store the data in a hosted Mongo database, e.g. MongoDB Atlas, for subsequent search and retrieval. Ensure the URL of the article is included to enable comparison to the original.
    - Write an API that provides access to the content in the mongo database.
    - Bonus: The user should be able to search the articles' text by keyword.

    + Setup Environment & Run the WebCrawler :
      % `www.bbc.com` -> the news website used in this web application

    % Initialize Virtual Environment :

    $ virtualenv -p python3 venv
	$ source ./venv/bin/activate
	$ pip install -r requirements.txt

    $ touch .env

    -> paste this two variables

         MONGODB_HOST_DEV=mongodb+srv://mongodb:data-engineering123@de-cluster-cgltu.mongodb.net/newsdb?retryWrites=true&w=majority
         MONGODB_HOST_TEST=mongodb+srv://mongodb:data-engineering123@de-cluster-cgltu.mongodb.net/newsdb-test?retryWrites=true&w=majority

    % Test All Endpoints :

    $ export environment=testing
	$ python tests.py

    % Launch the web app :

    $ source ./venv/bin/activate
	$ export FLASK_APP=manage.py
	$ flask run

    % Endpoints Description :

    $ Post http://127.0.0.1:5000/crawler/articles/bbc.com                   | Scrape All Articles in the `bbc.com` website and save them in the database.
    $ Post http://127.0.0.1:5000/crawler/article/world-africa-53040513      | Scrape The Article in this url : `https://www.bbc.com/news/world-africa-53040513` and save the content in the database.
    $ Get http://127.0.0.1:5000/crawler/articles/bbc.com                    | Scrape All Articles in the `bbc.com` website, and get the contents in json format.
    $ Get http://127.0.0.1:5000/crawler/article/world-africa-53040513       | Scrape The Article in this url : `https://www.bbc.com/news/world-africa-53040513`,  and get the content in json format.
    $ Get http://127.0.0.1:5000/articles/                                   | Fetch all Articles From database, and get them in json format.
    $ Get http://127.0.0.1:5000/articles/usa                                | Fetch All Articles That Contains the keyword `usa` from database, and get them in json format.

