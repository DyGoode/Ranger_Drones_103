from functools import wraps

import secrets

from flask import request, jsonify, json

from drone_inventory.models import User

import decimal


def token_required(our_flask_function):
    @wraps(our_flask_function)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token'].split(' ')[1]
            print(token)

        if not token:
            return jsonify({'message': 'Token is Missing!'}), 401

        try:
            current_user_token = User.query.filter_by(token = token).first()
            print(current_user_token)
            if not current_user_token or current_user_token.token != token:
                # current_user_token is referncing the queried User
                # current_user_token.token is referencin the User.token
                return jsonify({'message': 'Token is Invalid!'})

        except:
            owner = User.query.filter_by(token=token).first()
            # owner & current_user_token are referencing the same User
            if token != owner.token and secrets.compare_digest(token, owner.token):
                return jsonify({'message': 'Token is invalid!'})

        return our_flask_function(current_user_token, *args, **kwargs)
    
    return decorated



class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            #Convert decimal instances (numerics) into strings
            return str(obj)
        return super(JSONEncoder, self).default(obj)

        



        



