import os
import csv
import json

import tweepy
from flask import Flask, render_template

from config import config

config_name = os.getenv('DEV_ENV') or 'production'
app = Flask(__name__)
app.config.from_object(config[config_name])


@app.route("/")
def index():
    auth = tweepy.OAuthHandler(app.config['CONSUMER_KEY'],
                               app.config['CONSUMER_SECRET'])
    auth.secure = True
    auth.set_access_token(app.config['ACCESS_TOKEN'],
                          app.config['ACCESS_SECRET'])
    api = tweepy.API(auth)
    timeline = tweepy.Cursor(
        api.user_timeline, count=10, id=app.config['ACCOUNT_NAME']).items(10)

    tweets_list = []

    for tweet in timeline:
        data = extract_tweet_data(tweet)
        tweets_list.append(data)

    geojson_obj = format_to_geo_json(tweets_list)
    write_to_json_file(geojson_obj)

    return render_template('base.html', tweets=tweets_list)


def format_to_geo_json(tweets_list):
    """
    This function takes a list of dictionaries and returns
    a dictionary object (in the format of geojson http://geojson.org/)
    with all the existing coordinates.
    """
    geo_data = {
        "type": "FeatureCollection",
        "features": []
    }

    for item in tweets_list:
        if 'coordinates' in item:
            for coordinate in item['coordinates']:
                geo_data_feature = {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": coordinate.items()[0][1]
                    }
                }
                geo_data['features'].append(geo_data_feature)
    return geo_data


def write_to_json_file(geojson_obj):
    """
    This function writes the geojson object to a json file,
    so that the json file can be read by the `map.js`
    """
    with open(app.config['GEO_DATA_FILE'], 'wb') as fp:
        json.dump(geojson_obj, fp, indent=4)


def extract_tweet_data(tweet):
    """
    This function extracts specific data from each tweet,
    such as `hashtags` and checks if each hashtag exists has a
    country from the countries_coordinates.csv in order to get
    the country coordinates.

    Data is returned in the form of a dictionary.

    Example of data retuned:

    data = {
        'username': u'John Doe',
        'text': u"#India #Pakistan Lorem ipsum, ipsum",
        'hashtags': ['India', 'Pakistan'],
        'id': 778513303517659136,
        'coordinates': [
            {'India': [79.685401, 23.078953]},
            {'Pakistan': [69.642966, 29.899236]}
        ]
    }
    """
    data = {}
    data['username'] = tweet.user.name
    data['text'] = tweet.text
    data['id'] = tweet.id

    hashtags = tweet.entities['hashtags']
    if hashtags:
        data['hashtags'] = [str(htag['text']) for htag in hashtags]
        data['coordinates'] = []

        with open(app.config['COUNTRIES_COORDINATES']) as f:
            reader = csv.DictReader(f)
            for row in reader:
                for tag in data['hashtags']:
                    if tag == row['Country']:
                        data['coordinates'].append(
                            {tag: [float(row['Lg']), float(row['Lt'])]}
                        )
    return data


if __name__ == '__main__':
    app.run()
