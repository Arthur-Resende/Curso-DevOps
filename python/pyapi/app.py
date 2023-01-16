"""Simple flask API, handles requests and sends database items in JSON format as response"""

from flask import Flask, request
from flask_httpauth import HTTPBasicAuth
from db import database, USER_DATA

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
auth = HTTPBasicAuth()

@auth.verify_password
def verify(user, password):
    if not (user and password):
        return False
    return USER_DATA[user] == password

# GET request handler to get entire database
@app.route("/people", methods=["GET"])
def get_all_database():
    return database

# data cleaner, makes sure data follows specifications
def data_cleaner(data, field):
    if field.lower() == "id":
        return int(float(data))
    elif field.lower() == "first_name":
        return str(data).replace('-', ' ').replace('_', ' ').title()
    elif field.lower() == "last_name":
        return str(data).replace('-', ' ').replace('_', ' ').title()
    elif field.lower() == "email":
        return str(data).lower()

# GET request handler to get specific person, by value in field
@app.route("/people/<key>/<value>", methods=["GET"])
def get_person_by_field(key, value):
    counter = 0
    person_list = []
    for person in database:
        if data_cleaner(value, key) == person[key]:
            person_list.append(database[counter])
        counter += 1
    return person_list if person_list else f"No person found with that {key.replace('_', ' ')}"

# POST request handler to add one or more horses to database
@app.route("/people/add", methods=["POST"])
@auth.login_required
def add_person():
    # Verify if request is of type list, meaning more than one horse will be added
    if isinstance(request.json, list):
        person_list = []
        counter = 1
        for item in request.json:
            person_list.append({
                "id": len(database) + counter,
                "first_name": data_cleaner(item["first_name"], "first_name"),
                "last_name": data_cleaner(item["last_name"], "last_name"),
                "email": data_cleaner(item["email"], "email")
            })
            counter += 1
        database.extend(person_list)
        return {
            "message": "Data added successfully to database",
            "data": person_list
        }

    # if not of type list, must be type dict/json, meaning only one person will be added
    else:
        person = {
            "id": len(database) + 1,
            "first_name": data_cleaner(request.json["first_name"], "first_name"),
            "last_name": data_cleaner(request.json["last_name"], "last_name"),
            "email": data_cleaner(request.json["email"], "email")
        }
        database.append(person)
        return {
            "message": "Data added successfully to database",
            "data": person
        }

# DELETE request handler to delete one or more person
@app.route("/people/delete", methods=["DELETE"])
@auth.login_required
def delete_data():
    # Verify if request is of type list, meaning more than one person will be deleted
    if isinstance(request.json, list):
        for item in request.json:
            request_id = data_cleaner(item["id"], "id")
            del database[request_id - 1]
        return {"message": "Data deleted successfully"}

    # if not of type list, must be type dict/json, meaning only one person will be deleted
    else:
        request_id = data_cleaner(request.json["id"], "id")
        for item in database:
            if item["id"] == request_id:
                del database[request_id - 1]
                return {"message": "Data deleted successfully"}
        return {"message": "Id not in database"}

# PUT request handler to update one or more person
@app.route("/people/update", methods=["PUT"])
@auth.login_required
def update_horse():
    print(request.json)
    # Verify if request is of type list, meaning more than one person will be updated
    if isinstance(request.json, list):
        for request_item in request.json:
            for db_item in database:
                if int(db_item["id"]) == int(data_cleaner(request_item["id"], "id")):
                    db_item_id = db_item["id"] - 1
                    database[db_item_id]["first_name"] = data_cleaner(request_item["first_name"], "first_name")
                    database[db_item_id]["last_name"] = data_cleaner(request_item["last_name"], "last_name")
                    database[db_item_id]["email"] = data_cleaner(request_item["email"], "email")
        return {
            "message": "data updated successfully",
            "data": database
        }

    # if not of type list, must be type dict/json, meaning only one person will be updated
    else:
        request_id = data_cleaner(request.json["id"], "id")
        for item in database:
            if item["id"] == request_id:
                database[request_id - 1]["first_name"] = data_cleaner(request.json["first_name"], "first_name")
                database[request_id - 1]["last_name"] = data_cleaner(request.json["last_name"], "last_name")
                database[request_id - 1]["email"] = data_cleaner(request.json["email"], "email")
                break

        return {
            "message": "data updated successfully",
            "data": database[request_id - 1]
        }
