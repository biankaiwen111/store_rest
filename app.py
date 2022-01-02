import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://rfdrvnayhlzbum:0e96a8cfe8ea7bbb8dd1ccd071582d4397ab8a8520a1ec93cecdc85650186085@ec2-34-236-87-247.compute-1.amazonaws.com:5432/daspf8v0jopt0o"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "kevishax"
api = Api(app)


jwt = JWT(app, authenticate, identity)

api.add_resource(Store, "/store/<string:name>")
api.add_resource(StoreList, "/stores")
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")


if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)