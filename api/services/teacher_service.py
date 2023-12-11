from ..entites.teacher import Teacher
from ..models import teacher_model
from ..paginate import paginate
from ..schemas import teacher_schema
from api import db


def remove_teacher(teacher: teacher_model.Teacher):
    db.session.delete(teacher)
    db.session.commit()


def update_teacher(prev_teacher: teacher_model.Teacher, teacher: Teacher):
    prev_teacher.name = teacher.name
    prev_teacher.age = teacher.age
    db.session.commit()

    return prev_teacher


def create_teacher(teacher: Teacher):
    teacher_db = teacher_model.Teacher(name=teacher.name, age=teacher.age)
    db.session.add(teacher_db)
    db.session.commit()

    return teacher_db


def list_teachers():
    cs = teacher_schema.TeacherSchema(many=True)
    return paginate(teacher_model.Teacher, cs)


def get_teacher(id: int):
    return teacher_model.Teacher.query.filter_by(id=id).first()
