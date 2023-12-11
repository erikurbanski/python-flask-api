from flask_restful import Resource
from api import api
from flask import request, make_response, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import timedelta
from ..schemas import login_schema
from ..entites import user
from ..services import user_service

class LoginList(Resource):
    def post(self):
        cs = login_schema.LoginSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            email = request.json['email']
            password = request.json['password']

            user = user_service.get_user_by_email(email)

            if user and user.verify_password(password):
                access_token = create_access_token(identity=user.id, expires_delta=timedelta(seconds=100))
                refresh_token = create_refresh_token(identity=user.id)

                return make_response(jsonify({
                    'access_token': access_token,
                    'refresh_token': refresh_token,
                    'message': 'Login realizado com sucesso'
                }), 201)
            
            return make_response('As credenciais estão invalídas', 404)

api.add_resource(LoginList, '/login')
