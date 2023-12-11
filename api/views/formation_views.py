from flask_restful import Resource
from api import api
from flask import request, make_response, jsonify
from flask_jwt_extended import jwt_required
from ..schemas import formation_schema
from ..entites import formation
from ..services import formation_service


class FormationList(Resource):
    @jwt_required()
    def get(self):
        return formation_service.list_formations()

    @jwt_required()
    def post(self):
        cs = formation_schema.FormationSchema()
        validate = cs.validate(request.json)

        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json['name']
            description = request.json['description']
            teachers = request.json['teachers']

            new_formation = formation.Formation(name=name, description=description, teachers=teachers)
            result = cs.jsonify(formation_service.create_formation(new_formation))

            return make_response(result, 201)


class FormationDetail(Resource):
    @jwt_required()
    def get(self, id):
        formation = formation_service.get_formation(id)

        if formation is None:
            return make_response("Formação não encontrada", 404)

        cs = formation_schema.FormationSchema()
        return make_response(cs.jsonify(formation), 200)

    @jwt_required()
    def put(self, id):
        formation_db = formation_service.get_formation(id)

        if formation_db is None:
            return make_response("Formação não encontrada", 404)

        cs = formation_schema.FormationSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json['name']
            description = request.json['description']
            teachers = request.json['teachers']

            update_formation = formation.Formation(name=name, description=description, teachers=teachers)
            result = cs.jsonify(formation_service.update_formation(formation_db, update_formation))

            return make_response(result, 200)

    @jwt_required()
    def delete(self, id):
        formation_db = formation_service.get_formation(id)

        if formation_db is None:
            return make_response("Formação não encontrada!", 404)

        formation_service.remove_formation(formation_db)
        return make_response("Formação removida com sucesso!", 200)


api.add_resource(FormationList, '/formations')
api.add_resource(FormationDetail, '/formations/<int:id>')
