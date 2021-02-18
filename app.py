from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from db import db

app = Flask(__name__)
# specifies the location of the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # we don't want Flask's modification tracker
app.secret_key = "sudeep"  # needs to be complicated
api = Api(app)  # helps to make http operations easier


# this function runs before any http request is made - used for creation of rss. like tables
@app.before_first_request
def create_table():
    db.create_all()     # creates all necessary tables automatically


jwt = JWT(app, authenticate, identity)  # creates a new endpoint /auth which returns the JWT token

# resoures which the user can interact with
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)    # initialises the DB for the app
    app.run(port=5000, debug=True)
