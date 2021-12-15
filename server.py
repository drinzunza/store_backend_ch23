"""
  Desc: Backend for the online store
Author: Sergio Inzunza
"""

from flask import Flask, abort, request, render_template
from mock_data import catalog
import json
from config import db, json_parse

app = Flask(__name__)

about_me = {
    "name": "Sergio",
    "last": "Inzunza",
    "age": 35,
    "hobbies": [],
    "address": {
        "street": "42 evergreen",
        "city": "Springfield"
    }
}


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return f"{about_me['name']} {about_me['last']}"



#***********************************************************
#***************** API ENDPOINTS ***************************
#***********************************************************


@app.route("/api/catalog", methods=["get"])
def retrieve_catalog():
  # read data from the database (with no filter)
  cursor = db.products.find({})
  list = []
  for prod in cursor:    
    list.append(prod)

  return json_parse(list) # parse catalog into a JSON string and return it



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

  return abort(404) # return a 404 (not found) error




@app.route("/api/catalog/<category>")
def get_product_by_category(category):
  res = []
  for prod in catalog:
    if prod["category"] == category:
      res.append(prod)

  return json.dumps(res)




@app.route("/api/products/cheapest")
def get_cheapest_product():
  
  cheapest_prod = catalog[0]
  for prod in catalog:
    if (prod["price"] < cheapest_prod["price"]):
      cheapest_prod = prod

  return json.dumps(cheapest_prod)




@app.route("/api/products/categories")
def get_unique_categories():
  categories = []
  for prod in catalog:
      cat = prod["category"]
      if cat not in categories:
          categories.append(cat)
      
  return json.dumps(categories)





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




