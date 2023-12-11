from api import ma
from ..models import teacher_model
from marshmallow import fields


class TeacherSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = teacher_model.Teacher
        load_instance = True
        fields = ("id", "name", "age")

    name = fields.String(required=True)
    age = fields.Integer(required=True)

    _links = ma.Hyperlinks(
        {
            "get": ma.URLFor("teacherdetail", values=dict(id="<id>")),
            "put": ma.URLFor("teacherdetail", values=dict(id="<id>")),
            "delete": ma.URLFor("teacherdetail", values=dict(id="<id>"))
        }
    )
