from flask import *
from markupsafe import escape
from db import database

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# GET request handler to get entire database
@app.route('/horses', methods=['GET'])
def get_all_database():
    return database

# GET request handler to get specific horse, by name
@app.route('/horses/<horse_name>', methods=['GET'])
def get_specific_horse(horse_name):
    safe_horse_name = escape(horse_name)
    counter = 0
    for horse in database:
        if safe_horse_name.lower() == horse['name'].lower():
            return database[counter]
        counter += 1
    return "horse not found"

# POST request handler to add one or more horses to database
@app.route('/horses/add', methods=['POST'])
def add_horse():
    # Verify if request is of type list, meaning more than one horse will be added
    if type(request.json) == type([]):
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
    if type(request.json) == type([]):
        for item in request.json:
            del database[item['id'] - 1]
        return {"message": "Horses deleted successfully"}

    # if not of type list, must be type dict/json, meaning only one horse will be deleted
    else:
        id = request.json['id']
        for item in database:
            if item['id'] == id:
                del database[id - 1]
                return {"message": "Horse deleted successfully"}

@app.route('/horses/update', methods=['PUT'])
def update_horse():
    # Verify if request is of type list, meaning more than one horse will be updated
    if type(request.json) == type([]):
        for request_item in request.json:
            for db_item in database:
                if db_item['id'] == request_item['id']:
                    db_item_id = db_item['id'] - 1
                    database[db_item_id]['name'] = request_item['name']
        return {
            "message": "Horse list deleted successfully",
            "data": database
        }
    
    # if not of type list, must be type dict/json, meaning only one horse will be updated
    else:
        id = request.json['id']
        for item in database:
            if item['id'] == id:
                database[id - 1]['name'] = request.json['name']
                break

        return {
            "message": "Horse updated successfully",
            "data": database[id - 1]
        }