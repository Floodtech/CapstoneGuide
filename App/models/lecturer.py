from App.database import db
from .user import User


class Lecturer(User):
    lecturerId = db.Column(db.Integer, unique=True)

    def __init__(self, lecturerId):
        self.lecturerId = lecturerId