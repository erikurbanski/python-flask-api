from api import db
from .teacher_model import Teacher

# many-to-many relation
teacher_formation = db.Table(
    'teacher_formation',
    db.Column('teacher_id', db.Integer, db.ForeignKey('teachers.id'), primary_key=True, nullable=False),
    db.Column('formation_id', db.Integer, db.ForeignKey('formations.id'), primary_key=True, nullable=False),
)

class Formation(db.Model):
    __tablename__ = 'formations'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    teachers = db.relationship(Teacher, secondary="teacher_formation", back_populates="formations")
