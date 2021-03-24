Project: IMDB (International Movie Database) Scraping automation App

dependendencies to install before executing: 
python3, scrapy, numpy, scrapy, pandas, google-api-python-client, google-auth-httplib2, google-auth-oauthlib


Before startng the app please write in the console and press enter:
"pip install scrapy numpy pandas ..."
 pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

To start the app go to the imdb folder and write in the console:
"scrapy crawl imdb_movie" and press enter

Then please wait until the scraping is finished, this should take at least 2 minutes...

When the scraping is finished please type in the console the following to start

"python cast_members.py"

go to "https://developers.google.com/drive/api/v3/quickstart/python"

click enable drive.

In resulting dialog click DOWNLOAD CLIENT CONFIGURATION and save the file credentials.json to your working directory.
After start the "...." py and grant authorization to the script.



