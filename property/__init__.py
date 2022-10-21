from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import googlemaps
import pprint
import time
# from GoogleMapsAPIKEY import get_my_key
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///property.db'
app.config['SECRET_KEY'] = 'db6eb3f21b7b0e797431ef90'
db = SQLAlchemy(app)
#
# # API_KEY = get_my_key()
# gmaps = googlemaps.Client(key='AIzaSyDLrrrVK8iu9MLBQCaE3mGPpxYpjSSTfUg')
# # payload = {}
# # headers = {}
# url = "https://maps.googleapis.com/maps/api/place/autocomplete/json?input=amoeba&types=establishment&location=37.76999%2C-122.44696&radius=500&key=AIzaSyDLrrrVK8iu9MLBQCaE3mGPpxYpjSSTfUg"
# address_result = requests.request("GET", url)
# print(address_result.text)


from property import routes
