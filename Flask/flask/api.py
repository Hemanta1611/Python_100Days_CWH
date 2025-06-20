# Working with API's -- Json

from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# we can perform below task and verify all api's/routes in postman

# Initial Data in my to do list
items = [
    {"id": 1, "name": "Hemanta", "description": "Complete Python Revision"},
    {"id": 2, "name": "Eat", "description": "Eat healthy food"},
    {"id": 3, "name": "Game", "description": "Play games"},
    {"id": 4, "name": "Outing", "description": "Go for outing"}
]

@app.route("/")
def home():
    return "<html><h1>Welcome to the sample TO-DO List App</h1></html>"

# Get all items
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)           

# get a specific item by ID
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)

# post: create a new task
@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({'error': 'Missing name in request'}), 400
    item = {
        'id': items[-1]['id'] + 1,
        'name': request.json['name'],
        'description': request.json.get('description', '')
    }
    items.append(item)
    return jsonify(item), 201

# put : update an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def add_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({'error': 'Item not found'}), 404
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)

# delete: delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({'error': 'Item not found'}), 404
    items.remove(item)
    return jsonify({'message': 'Item deleted successfully'})

if __name__=="__main__":
    app.run(debug=True)