from ..entites.formation import Formation
from ..models import formation_model
from ..schemas import formation_schema
from .teacher_service import get_teacher
from ..paginate import paginate
from api import db


def remove_formation(formation: formation_model.Formation):
    db.session.delete(formation)
    db.session.commit()


def update_formation(prev_formation: formation_model.Formation, formation: Formation):
    prev_formation.name = formation.name
    prev_formation.description = formation.description
    prev_formation.teachers = []
    for i in formation.teachers:
        teacher = get_teacher(i)
        prev_formation.teachers.append(teacher)
    db.session.commit()

    return prev_formation


def create_formation(formation: Formation):
    formation_db = formation_model.Formation(name=formation.name, description=formation.description)
    for i in formation.teachers:
        teacher = get_teacher(i)
        formation_db.teachers.append(teacher)
    db.session.add(formation_db)
    db.session.commit()

    return formation_db


def list_formations():
    cs = formation_schema.FormationSchema(many=True)
    return paginate(formation_model.Formation, cs)


def get_formation(id: int):
    return formation_model.Formation.query.filter_by(id=id).first()
