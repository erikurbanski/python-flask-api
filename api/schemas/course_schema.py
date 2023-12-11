from api import ma
from ..models import course_model
from marshmallow import fields


class CourseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = course_model.Course
        load_instance = True
        fields = ("id", "name", "description", "published_at", "formation", "_links")

    name = fields.String(required=True)
    description = fields.String(required=True)
    published_at = fields.Date(required=True)
    formation = fields.String(required=True)

    _links = ma.Hyperlinks(
        {
            "get": ma.URLFor("coursedetail", values=dict(id="<id>")),
            "put": ma.URLFor("coursedetail", values=dict(id="<id>")),
            "delete": ma.URLFor("coursedetail", values=dict(id="<id>"))
        }
    )