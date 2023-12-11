from flask_restful import Resource
from api import api
from flask import request, make_response, jsonify
from flask_jwt_extended import jwt_required
from ..decorator import admin_required
from ..schemas import course_schema
from ..entites import course
from ..services import course_service, formation_service

class CourseList(Resource):
    @jwt_required()
    def get(self):
        return course_service.list_courses()

    @admin_required
    def post(self):
        cs = course_schema.CourseSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json['name']
            description = request.json['description']
            published_at = request.json['published_at']
            formation = request.json['formation']
            formation_db = formation_service.get_formation(formation)

            if formation_db is None:
                return make_response("Formação não encontrada", 404)

            new_course = course.Course(
                name=name,
                description=description,
                published_at=published_at,
                formation=formation_db,
            )
            result = cs.jsonify(course_service.create_course(new_course))

            return make_response(result, 201)


class CourseDetail(Resource):
    @jwt_required()
    def get(self, id):
        course = course_service.get_course(id)

        if course is None:
            return make_response("Curso não encontrado", 404)

        cs = course_schema.CourseSchema()
        return make_response(cs.jsonify(course), 200)

    @admin_required
    def put(self, id):
        course_db = course_service.get_course(id)

        if course_db is None:
            return make_response("Curso não encontrado", 404)

        cs = course_schema.CourseSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json['name']
            description = request.json['description']
            published_at = request.json['published_at']
            formation = request.json['formation']
            formation_db = formation_service.get_formation(formation)

            if formation_db is None:
                return make_response("Formação não encontrada", 404)

            update_course = course.Course(
                name=name,
                description=description,
                published_at=published_at,
                formation=formation_db,
            )
            result = cs.jsonify(course_service.update_course(course_db, update_course))

            return make_response(result, 200)

    @admin_required
    def delete(self, id):
        course_db = course_service.get_course(id)

        if course_db is None:
            return make_response("Curso não encontrado!", 404)

        course_service.remove_course(course_db)

        return make_response("Curso removido com sucesso!", 200)


api.add_resource(CourseList, '/courses')
api.add_resource(CourseDetail, '/courses/<int:id>')
