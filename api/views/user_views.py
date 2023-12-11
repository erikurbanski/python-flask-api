from flask_restful import Resource
from api import api, jwt
from flask import request, make_response, jsonify
from ..schemas import user_schema
from ..entites import user
from ..services import user_service
import uuid

class UserList(Resource):
    @jwt.additional_claims_loader
    def add_claims_to_token(identity):
        user = user_service.get_user_by_id(identity)
        roles = 'user'
        if user.is_admin:
            roles = 'admin'

        return {'roles': roles}
        

    def post(self):
        cs = user_schema.UserSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json['name']
            email = request.json['email']
            password = request.json['password']
            is_admin = request.json['is_admin']
            api_key = str(uuid.uuid4())
            print(api_key)
            new_user = user.User(name=name, email=email, password=password, is_admin=is_admin, api_key=api_key)
            result = cs.jsonify(user_service.create_user(new_user))

            return make_response(result, 201)


api.add_resource(UserList, '/users')
