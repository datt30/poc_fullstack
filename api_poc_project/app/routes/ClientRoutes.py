from app.models import Client as clientModel
from flask import request, jsonify
from app import app, db


@app.route('/poc/v1/clients/', methods=['GET'])
def get_clients():
    try:
        clients_list = clientModel.Client.query.all()
        return jsonify({'clients': [client.serialize() for client in clients_list]}), 201
    except Exception as e:
        # usually for server security, the error must be stored in a log,
        # but for practical purposes of the poc we will show it in the response
        return jsonify({'message': 'server error', 'error': str(e)}), 500


@app.route('/poc/v1/client/<int:id>/', methods=['GET'])
def get_client(id):
    try:
        return jsonify({'client': clientModel.Client.query.get(id).serialize()}), 201
    except Exception as e:
        return jsonify({'message': 'server error', 'error': str(e)}), 500


@app.route('/poc/v1/client/', methods=['POST'])
def create_client():
    content = request.json

    if not content or not 'identityNumber' in content:
        return jsonify({'message': 'bad request'}), 400
    else:
        try:
            client = clientModel.Client(
                content['identityNumber'],
                content['age'],
                content['clientName'],
                content['clientSurname'],
            )
            db.session.add(client)
            db.session.commit()
            return jsonify({'message': 'success'}), 201
        except Exception as e:
            return jsonify({'message': 'server error', 'error': str(e)}), 500


@app.route('/poc/v1/client/<int:id>', methods=['DELETE'])
def delete_client(id):
    try:
        clientModel.Client.query.filter(clientModel.Client.identity_number == id).delete()
        db.session.commit()
        return jsonify({'message': 'success delete'}), 201
    except Exception as e:
        return jsonify({'message': 'server error', 'error': str(e)}), 500


@app.route('/poc/v1/client/<int:id>', methods=['PUT'])
def update_client(id):
    content = request.json
    try:
        client = clientModel.Client.query.filter(clientModel.Client.identity_number == id).one()
        client.identity_number = content['identityNumber']
        client.age = content['age']
        client.client_name = content['clientName']
        client.client_surname = content['clientSurname']
        db.session.commit()
        return jsonify({'message': 'success update'}), 201
    except Exception as e:
        return jsonify({'message': 'server error', 'error': str(e)}), 500
