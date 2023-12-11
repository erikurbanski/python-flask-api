from flask_restful import Resource
from api import api
from flask import request, make_response, jsonify
from flask_jwt_extended import jwt_required
from ..schemas import teacher_schema
from ..entites import teacher
from ..services import teacher_service


class TeacherList(Resource):
    @jwt_required()
    def get(self):
        return teacher_service.list_teachers()

    @jwt_required()
    def post(self):
        cs = teacher_schema.TeacherSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json['name']
            age = request.json['age']

            new_teacher = teacher.Teacher(name=name, age=age)
            result = cs.jsonify(teacher_service.create_teacher(new_teacher))

            return make_response(result, 201)


class TeacherDetail(Resource):
    @jwt_required()
    def get(self, id):
        teacher = teacher_service.get_teacher(id)

        if teacher is None:
            return make_response("Professor não encontrado", 404)

        cs = teacher_schema.TeacherSchema()
        return make_response(cs.jsonify(teacher), 200)

    @jwt_required()
    def put(self, id):
        teacher_db = teacher_service.get_teacher(id)

        if teacher_db is None:
            return make_response("Professor não encontrado", 404)

        cs = teacher_schema.TeacherSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json['name']
            age = request.json['age']

            update_teacher = teacher.Teacher(name=name, age=age)
            result = cs.jsonify(teacher_service.update_teacher(teacher_db, update_teacher))

            return make_response(result, 200)

    @jwt_required()
    def delete(self, id):
        teacher_db = teacher_service.get_teacher(id)

        if teacher_db is None:
            return make_response("Professor não encontrado!", 404)

        teacher_service.remove_teacher(teacher_db)

        return make_response("Professor removido com sucesso!", 200)


api.add_resource(TeacherList, '/teachers')
api.add_resource(TeacherDetail, '/teachers/<int:id>')
