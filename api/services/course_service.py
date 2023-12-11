from ..entites.course import Course
from ..models import course_model
from ..paginate import paginate
from ..schemas import course_schema
from api import db


def remove_course(course: course_model.Course):
    db.session.delete(course)
    db.session.commit()


def update_course(prev_course: course_model.Course, course: Course):
    prev_course.name = course.name
    prev_course.description = course.description
    prev_course.published_at = course.published_at
    prev_course.formation = course.formation
    db.session.commit()

    return prev_course


def create_course(course: Course):
    course_db = course_model.Course(
        name=course.name,
        description=course.description,
        published_at=course.published_at,
        formation=course.formation,
    )
    db.session.add(course_db)
    db.session.commit()

    return course_db


def list_courses():
    cs = course_schema.CourseSchema(many=True)
    return paginate(course_model.Course, cs)


def get_course(id: int):
    return course_model.Course.query.filter_by(id=id).first()
