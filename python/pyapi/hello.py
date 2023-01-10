from flask import *
from db import database

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/horses', methods=['GET'])
def index():
    return make_response(
        jsonify(database)
    )

@app.route('/horses', methods=['POST'])
def add_horse():
    horse = {
        "id": len(database) + 1,
        "name": request.json['name']
    }
    database.append(horse)
    return make_response(
        jsonify(
            message = 'Horse added successfully',
            data = horse
        )
    )

@app.route('/horses', methods=['DELETE'])
def delete_horse():
    id = request.json['id']
    deleted_horse = database[id - 1]
    for item in database:
        if item['id'] == id:
            del database[id - 1]
            break

    return make_response(
        jsonify(
            message = 'Horse deleted successfully',
            data = deleted_horse
        )
    )

@app.route('/horses', methods=['PUT'])
def update_horse():
    id = request.json['id']
    for item in database:
        if item['id'] == id:
            database[id - 1]['name'] = request.json['name']
            break

    return make_response(
        jsonify(
            message = 'Horse deleted successfully',
            data = database[id - 1]
        )
    )