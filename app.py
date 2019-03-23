from user import UserRegister

from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'my item',
                'price': 15.99
            }
        ]
    },
    {
        'name': 'wtf',
        'items': [
            {
                'name': 'my item',
                'price': 15.99
            }
        ]
    }
]


@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    item = {
        "name": request_data['name'],
        "price": 15.99
    }
    for store in stores:
        if store['name'] == name:
            store['items'].append(item)
            return jsonify(item)
    return jsonify({'message': 'did not find store'})


@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({"items": store['items']})
    return jsonify({'message': 'store not found'})


app.run(port=3000)
