"""Simple flask API, handles requests and sends database items in JSON format as response"""

from flask import Flask, request
from markupsafe import escape
from db import database

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# GET request handler to get entire database
@app.route('/people', methods=['GET'])
def get_all_database():
    return database

# data cleaner, makes sure data follows specifications
def data_cleaner(request_data):
    if isinstance(request_data, str):
        if request_data.isnumeric():
            return int(request_data)
        else:
            try:
                return int(float(request_data))

            except:
                return request_data.replace('_', ' ').replace('-', ' ').lower()

    elif isinstance(request_data, float):
        return int(request_data)
    elif isinstance(request_data, int):
        return request_data
    else:
        print("type not supported yet")

# GET request handler to get specific person, by value in field
@app.route('/people/<key>/<value>', methods=['GET'])
def get_person_by_field(key, value):
    counter = 0
    person_list = []
    for person in database:
        if data_cleaner(value) == data_cleaner(person[key]):
            person_list.append(database[counter])
        counter += 1
    return person_list if person_list else f"no person found with that {key.replace('_', ' ')}"

# POST request handler to add one or more horses to database
@app.route('/horses/add', methods=['POST'])
def add_horse():
    # Verify if request is of type list, meaning more than one horse will be added
    if isinstance(request.json, list):
        horse = []
        counter = 1
        for item in request.json:
            horse.append({
                "id": len(database) + counter,
                "name": item['name']
            })
            counter += 1
        database.extend(horse)
        return {
            "message": "Horse list extended successfully",
            "data": horse
        }

    # if not of type list, must be type dict/json, meaning only one horse will be added
    else:
        print(data_cleaner(request.json['name']))
        horse = {
            "id": len(database) + 1,
            "name": request.json['name']
        }
        database.append(horse)
        return {
            "message": "Horse added successfully",
            "data": horse
        }

# DELETE request handler to delete one or more horses
@app.route('/horses/delete', methods=['DELETE'])
def delete_horse():
    # Verify if request is of type list, meaning more than one horse will be deleted
    if isinstance(request.json, list):
        for item in request.json:
            del database[item['id'] - 1]
        return {"message": "Horses deleted successfully"}

    # if not of type list, must be type dict/json, meaning only one horse will be deleted
    else:
        request_id = request.json['id']
        for item in database:
            if item['id'] == request_id:
                del database[request_id - 1]
                return {"message": "Horse deleted successfully"}

@app.route('/horses/update', methods=['PUT'])
def update_horse():
    # Verify if request is of type list, meaning more than one horse will be updated
    if isinstance(request.json, list):
        for request_item in request.json:
            for db_item in database:
                if int(db_item['id']) == int(request_item['id']):
                    db_item_id = db_item['id'] - 1
                    database[db_item_id]['name'] = request_item['name']
        return {
            "message": "Horse list deleted successfully",
            "data": database
        }

    # if not of type list, must be type dict/json, meaning only one horse will be updated
    else:
        request_id = int(request.json['id'])
        for item in database:
            if item['id'] == request_id:
                database[request_id - 1]['name'] = request.json['name']
                break

        return {
            "message": "Horse updated successfully",
            "data": database[request_id - 1]
        }
