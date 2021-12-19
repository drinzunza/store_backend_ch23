"""
  Desc: Backend for the online store
Author: Sergio Inzunza
"""

from bson.objectid import ObjectId
from flask import Flask, abort, request, render_template
from mock_data import catalog
import json
from config import db, json_parse
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # WARNING: allow the server to be call from any client url

about_me = {
    "name": "Sergio",
    "last": "Inzunza",
    "age": 35,
    "hobbies": [],
    "address": {"street": "42 evergreen", "city": "Springfield"},
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return f"{about_me['name']} {about_me['last']}"


# ***********************************************************
# ***************** API ENDPOINTS ***************************
# ***********************************************************


@app.route("/api/catalog", methods=["get"])
def retrieve_catalog():
    # read data from the database (with no filter)
    cursor = db.products.find({})
    list = []
    for prod in cursor:
        list.append(prod)

    return json_parse(list)  # parse catalog into a JSON string and return it


@app.route("/api/catalog", methods=["post"])
def save_catalog():
    # get the payload (the object/data that client is sending)
    product = request.get_json()
    # save the product object to database
    db.products.insert_one(product)
    return json_parse(product)


@app.route("/api/product/<id>")
def get_product(id):
    # find in catalog the product with _id equal to id
    for prod in catalog:
        if prod["_id"] == id:
            return json.dumps(prod)

    return abort(404)  # return a 404 (not found) error


@app.route("/api/catalog/<category>")
def get_product_by_category(category):
    # mongo to search case insensitive we use Regular Expressions
    cursor = db.products.find({"category": category})
    list = []
    for prod in cursor:
        list.append(prod)

    return json_parse(list)


@app.route("/api/products/cheapest")
def get_cheapest_product():
    cursor = db.products.find({})
    pivot = cursor[0]
    for prod in cursor:
        if prod["price"] < pivot["price"]:
            pivot = prod

    return json_parse(pivot)


@app.route("/api/products/categories")
def get_unique_categories():
    # return the list (string) of UNIQUE categories
    categories = []
    cursor = db.products.find({})
    for prod in cursor:
        if not prod["category"] in categories:
            categories.append(prod["category"])

    # logic
    return json_parse(categories)


@app.route("/api/order", methods=["POST"])
def save_order():
    order = request.get_json()

    # sum the prices
    total = 0
    for prod in order["products"]:
        # get the prod from the database with that _id
        db_prod = db.products.find_one({"_id": ObjectId(prod["_id"])})
        price = db_prod["price"]
        quantity = prod["quantity"]
        total += price * quantity

    # validation
    if total <= 0:
        return abort(400)  # return bad request

    order["total"] = total
    db.orders.insert_one(order)
    return json_parse(order)


@app.route("/test/onetime/filldb")
def fill_db():
    for prod in catalog:
        #  remove the _id from the prod
        prod.pop("_id")

        # save the obj into the db
        db.products.insert_one(prod)

    return "Done!"


# TODO: remove debug before deploying
app.run(debug=True)
