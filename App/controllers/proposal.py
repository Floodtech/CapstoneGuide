from App.models import Proposal
from App.database import db
from .user import get_student

def add_proposal(student_id, rubric_id, proposal_nm, problem_desc, audience, solution_desc, approach,
                 num_members, functionalities, technologies, goals, benefit, sustain, notes):
    student = get_student(student_id)
    if student:
        proposal = Proposal(student, rubric_id, proposal_nm=proposal_nm, problem_desc=problem_desc, audience=audience, solution_desc=solution_desc,
                            approach=approach, num_members=num_members, requirements=functionalities, tools=technologies,
                              goals=goals, benefit=benefit, sustainability=sustain, notes=notes)
        student.proposals.append(proposal)
        db.session.add(proposal)
        db.session.commit()
        return proposal
    return None

def remove_proposal(student_id, proposal_id):
    proposal = Proposal.query.filter_by(student_id=student_id, id=proposal_id).first()
    if proposal:
        db.session.delete(proposal)
        res = db.session.commit()
        return res
    return None

def get_proposal(proposal_id):
    return Proposal.query.get(proposal_id)

def get_proposal_by_rubric(rubric_id):
    return Proposal.query.filter_by(rubric_id=rubric_id).first()

def get_user_proposal(proposal_id, student_id):
    proposal = Proposal.query.filter_by(student_id=student_id, id = proposal_id).first() 
    return proposal

def get_user_proposals(student_id):
    return Proposal.query.filter_by(student_id=student_id).all()

def get_all_proposals():
    return Proposal.query.all()
def get_last_proposal():
    return Proposal.query.order_by(Proposal.id.desc()).first()
