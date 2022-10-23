# importing libraries and packages
import snscrape.modules.twitter as sntwitter
from pymongo import MongoClient
import pandas as pd
import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie


# ---------------------Layouts for UI-----------------------------

# --Sidebar--
side = st.sidebar
search = side.text_input('Enter Keyword or Hashtag to be Searched')
from_date = side.date_input('From Date:')
to_date = side.date_input('To Date')
tweet_count = side.number_input('Tweet count to be Scraped', min_value = 1, max_value = 1000)
scrap = side.button('Scrap')

# --Main Container--
main = st.container()
title = main.title('Twitter Scraper')
head = main.header('Welcome fellow Data Enthusiast. :sunglasses: ')
describ = main.markdown('Kindly provide details for scraping data from Twitter for your future endeavors. :smirk:')

# Animation
def lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_ani = lottieurl('https://assets7.lottiefiles.com/packages/lf20_x17ybolp.json')
ani = st_lottie(lottie_ani, key = "hello")
anime = main.ani

# ---------------------Layouts for UI-----------------------------

# ---------------------SN Scraper-----------------------------

# Using TwitterSearchScraper to scrape data and append tweets to list
def scraper():
    global tweets_list1
    tweets_list1 = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f"{search} since:{from_date} until:{to_date}").get_items()):  # declare a username, from date and to date
        if i > (tweet_count - 1):  # number of tweets you want to scrape
            break
        tweets_list1.append(
         [tweet.date, tweet.id, tweet.url, tweet.content, tweet.user.username, tweet.replyCount, tweet.retweetCount, tweet.lang, tweet.source, tweet.likeCount])  # declare the attributes to be returned
    global tweets_df1

    # Converting into Dataframe
    tweets_df1 = pd.DataFrame(tweets_list1,
                              columns=['Datetime', 'Tweet Id', 'URL', 'Text', 'Username', 'ReplyCount', 'Retweet_Count',
                                       'Language', 'Source', 'Like_Count'])
    tweets_df = tweets_df1.head(5)
    display = main.table(data=tweets_df)

    # ------------------------Download as CSV--------------------------------
    @st.cache
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')

    csv = convert_df(tweets_df1)
    main.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='large_df.csv',
        mime='text/csv',
    )
    # ------------------------Download as CSV--------------------------------

    # ------------------------Upload to Database--------------------------------
    # main.button('Say hello', on_click=print_hello)

    # upload_df = main.button("Upload to Database")
    main.button("Upload to Database", on_click=upload_to_database)
        # # Making a Connection with MongoClient
        # client = MongoClient('localhost', 27017)
        # # database
        # db = client.database
        # # collection
        # collection = db.collection
        #
        # # Inserting the data into the Database
        # tweets_df1.reset_index(inplace=True)
        # data_dict = tweets_df1.to_dict("records")
        # collection.insert_many(data_dict)
    #     print('hello there')
    #     main.write('Uploaded to database successfully :sunglasses: ')
    # else:
    #     main.write('You can upload this data into your MongoDB')
        # ------------------------Upload to Database--------------------------------

# ---------------------SN Scraper-----------------------------
def upload_to_database():
    # Making a Connection with MongoClient
    client = MongoClient('localhost', 27017)
    # database
    db = client.database
    # collection
    collection = db.collection

    # Inserting the data into the Database
    tweets_df1.reset_index(inplace=True)
    data_dict = tweets_df1.to_dict("records")
    collection.insert_many(data_dict)
    main.write('Uploaded to database successfully :sunglasses: ')

def print_hello():
    main.write('hello there')

# ---------------------Making the Scraped data accessible-----------------------------
if scrap:
    scraper()







