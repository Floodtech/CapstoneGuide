from App.database import db
from datetime import datetime


class Proposal(db.Model):
    __tablename__ = 'proposal'
    proposalId = db.Column(db.Integer, primary_key=True)
    studentId = db.Column(db.Integer, db.ForeignKey('student.studentId'))
    rubricId = db.Column(db.Integer, db.ForeignKey('rubric.id'))
    problem_desc = db.Column(db.String)
    solution_desc = db.Column(db.String)
    notes = db.Column(db.String)
    functionalities = db.Column(db.String)
    technologies = db.Column(db.String)
    num_members = db.Column(db.Integer)
    created = db.Column(db.DateTime, default=datetime.utcnow)


    def __init__(self, studentId, rubricId, problem_desc, solution_desc,
                 num_members, notes, functionalities, technologies):
        self.studentId = studentId
        self.rubricId = rubricId
        self.problem_desc = problem_desc
        self.solution_desc = solution_desc
        self.num_members = num_members
        self.notes = notes
        self.functionalities = functionalities
        self.technologies = technologies
