# Twitter_Scraper_App

Today, data is scattered everywhere in the world. Especially in social media, there may be a big quantity of data on Facebook, Instagram, Youtube, Twitter, etc. This consists of pictures and films on Youtube and Instagram as compared to Facebook and Twitter. To get the real facts on Twitter, we want to scrape the data from Twitter. As a fellow Data Enthusiast, I have created user friendly Scraper App where you can easily obtain data from twitter for your future endeavour.

<img align="right" alt="coding" width="400" src="https://github.com/vasudevan-gomathy/Twitter_Scraper_App/blob/main/78999-data-scanning.gif">

## About the App
This App contains the feature to enter the keyword or Hashtag to be searched, select the date range and limit the tweet count need to be scraped. After scraping, the data will be displayed in the page and has a button to upload the data into **MongoDB Database** and **download the data into csv format**.

The Scraper creates a dataframe with:
-date, 
-id, 
-url, 
-tweet content, 
-user,
-reply count, 
-retweet count,
-language, 
-source, 
-like count.

![face](https://user-images.githubusercontent.com/85822284/197381637-be190df8-096e-495c-9a27-8af300bb315b.png)

## Python Packages utilised:
### SN Scrape

SNscrape is a scraper for social networking services (SNS). It scrapes things like user profiles, hashtags, or searches and returns the discovered items, e.g. the relevant posts.

The following services are currently supported:

Facebook: user profiles, groups, and communities (aka visitor posts)
Instagram: user profiles, hashtags, and locations
Mastodon: user profiles and toots (single or thread)
Reddit: users, subreddits, and searches (via Pushshift)
Telegram: channels
Twitter: users, user profiles, hashtags, searches, tweets (single or surrounding thread), list posts, and trends
VKontakte: user profiles
Weibo (Sina Weibo): user profiles
Requirements
snscrape requires Python 3.8 or higher. The Python package dependencies are installed automatically when you install snscrape.

Note that one of the dependencies, lxml, also requires libxml2 and libxslt to be installed.

Installation:

pip3 install snscrape

If you want to use the development version:

pip3 install git+https://github.com/JustAnotherArchivist/snscrape.git

for more details: https://github.com/JustAnotherArchivist/snscrape#readme

### Pymongo

pip install pymongo

For collecting data to MongoDB Database

### Pandas

pip install pandas

For converting JSON file into DataFrames
