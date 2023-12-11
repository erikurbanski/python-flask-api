from api import ma
from marshmallow import fields
from ..models import formation_model
from ..schemas import course_schema, teacher_schema


class FormationSchema(ma.SQLAlchemyAutoSchema):    
    class Meta:
        model = formation_model.Formation
        load_instance = True
        fields = ("id", "name", "description", "courses", "teachers")

    name = fields.String(required=True)
    description = fields.String(required=True)
    courses = fields.List(fields.Nested(course_schema.CourseSchema, only=('id', 'name')))
    teachers = ma.Nested(teacher_schema.TeacherSchema, many=True, only=('id', 'name'))

    _links = ma.Hyperlinks(
        {
            "get": ma.URLFor("formationdetail", values=dict(id="<id>")),
            "put": ma.URLFor("formationdetail", values=dict(id="<id>")),
            "delete": ma.URLFor("formationdetail", values=dict(id="<id>"))
        }
    )