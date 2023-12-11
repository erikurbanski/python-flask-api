from api import db
from ..models import formation_model


class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    published_at = db.Column(db.Date, nullable=False)

    formation_id = db.Column(db.Integer, db.ForeignKey('formations.id'))
    formation = db.relationship(formation_model.Formation, backref=db.backref('courses', lazy='dynamic'))
