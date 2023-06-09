from App.database import db
from .user import User

class Student(User):
    __tablename__ = 'student'
    studentId = db.Column(db.Integer, unique=True)

    def __init__(self, studentId):
        self.studentId = studentId