import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.main import create_app
from App.controllers import ( create_student, create_lecturer, get_stu_by_username, get_lect_by_username, get_all_students, get_all_lecturers,
                             add_rubric, get_user_rubric, get_all_rubrics,
                             add_proposal, get_proposal, get_all_proposals,
                             add_evaluation, get_user_evaluation,  get_all_evaluations)
# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def initialize():
    # db.drop_all()
    # db.create_all()
    # # rob = create_student('rob', 'robspass', 'rob@mycavehilluwi.edu', 'Rob', 'Renolds', 2222)
    # # steve = create_student('steve', 'stevepass', 'steve@mycavehilluwi.edu', 'Steve', 'Pass', 3333)
    # ai = create_lecturer('capadviosr', 'capadvisor', 'capadvisor@temp.com', 'Cap', 'Adivosr(AI)', 9999)
    # bob = create_lecturer('bob', 'bobspass', 'bob@mycavehilluwi.edu', 'bob', 'smith', 1111)
    # # cory = create_lecturer('cory', 'corypass', 'cory@mycavehilluwi.edu', 'Cory', 'Jones', 4444)
    # rubric = add_rubric('Default','For practice', 3, 5, 6, 6, 6, 1, 101)
    # cap_advisor = add_proposal(steve.id, rubric.id, 'Cap Advisor', 'Students do not always undertsand how to design capstone projects', 'SWEN and COMP students',
    #             'Students can submit capstone proposals to and have feedback', 'craete a web app which allows them submit proposal according to capstone rubric',
    #             3, 'students must submit proposals based on cirtera', 'flask MVC, python, GPT-3', 'students can understand what is required for capstone projects and begine their own',
    #               'SWEN and COMP students','manged by lecturer eventually',
    #             'May be revised')
    # flask_test = add_proposal(steve.id, rubric.id, 'Flask Test', 'Students do not always undertsand how to design capstone projects', 'SWEN and COMP students',
    #             'Students can submit capstone proposals to and have feedback', 'craete a web app which allows them submit proposal according to capstone rubric',
    #             2, 'students must submit proposals based on cirtera', 'flask MVC, python, GPT-3', 'students can understand what is required for capstone projects and begine their own',
    #               'SWEN and COMP students','manged by lecturer eventually',
    #             'May be revised')
    # solo = add_proposal(rob.id, rubric.id, 'Solo', 'Students do not always undertsand how to design capstone projects', 'SWEN and COMP students',
    #             'Students can submit capstone proposals to and have feedback', 'craete a web app which allows them submit proposal according to capstone rubric',
    #             5, 'students must submit proposals based on cirtera', 'flask MVC, python, GPT-3', 'students can understand what is required for capstone projects and begine their own',
    #               'SWEN and COMP students','manged by lecturer eventually',
    #             'May be revised')
    # add_evaluation('notes', 5, 7, 5, 3, 10, 5, cap_advisor.id, cory.id)
    # add_evaluation('crash', 10, 10, 1, 3, 10, 10, flask_test.id, bob.id)
    # add_evaluation('crash', 10, 10, 1, 3, 10, 10, solo.id, ai.id)
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# Lecturer Test
# eg : flask user <command>
lecturer_cli = AppGroup('lecturer', help='Lecturer object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@lecturer_cli.command("create", help="Creates a lecturer")
@click.argument("username", default="alexa")
@click.argument("password", default="alexapass")
@click.argument("email", default="alexander.atwell@uwi.edu")
@click.argument("first", default="Alex")
@click.argument("last", default="Atwell")
@click.argument("id", default=415001713)
def create_lecturer_command(username, password, email, id, first, last):
    create_lecturer(username, password, email, first, last, id)
    if get_lect_by_username(username):
        print(f'{username} created!')

# this command will be : flask lecturer create name password email firstname lastname uwi_id

@lecturer_cli.command("list", help="Lists lecturers in the database")
@click.argument("format", default="string")
def list_lecturers_command(format):
    if format == 'string':
        print(get_all_lecturers())

app.cli.add_command(lecturer_cli) # add the group to the cli

# Student Test
# eg : flask user <command>
student_cli = AppGroup('student', help='Student object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@student_cli.command("create", help="Creates a student")
@click.argument("username", default="danteb")
@click.argument("password", default="dantepass")
@click.argument("email", default="dante.blunt@uwi.edu")
@click.argument("first", default="Dante")
@click.argument("last", default="Blunt")
@click.argument("id", default=2222)
def create_student_command(username, password, email,  id, first, last):
    create_student(username, password, email, first, last, id)
    if get_stu_by_username(username):
        print(f'{username} created!')

# this command will be : flask student create name password email firstname lastname uwi_id

@student_cli.command("list", help="Lists students in the database")
@click.argument("format", default="string")
def list_students_command(format):
    if format == 'string':
        print(get_all_students())

app.cli.add_command(student_cli) # add the group to the cli


# Rubric Test
# eg : flask rurbric <command>
rubric = AppGroup('rubric', help='Rubric object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@rubric.command("create", help="Creates a dummy rubric")
@click.argument("notes", default="notes")
@click.argument("name", default="COMP")
def create_rubric_command(notes, name):
    add_rubric(name=name,notes=notes, novelty=5, relevance=5, feasibility=5,
                impact=5, sustainability=5, technology=5, lecturer_id=101)
    if(get_user_rubric(101, 1)):
        print(f'rubric created!')

@rubric.command("list", help="Lists all rubrics in the database")
def list_rubric_command():
    print(get_all_rubrics())

app.cli.add_command(rubric) 

# Proposal Test
# eg : flask proposal <command>
proposal = AppGroup('proposal', help='Proposal object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@proposal.command("create", help="Creates a dummy proposal")
@click.argument("student", default=1)
def create_proposal_command(student):
    prop = add_proposal(rubric_id=1, student_id=student, proposal_nm='Cap Advisor', problem_desc='Students can have their proposals evaluated early', audience='SWEN and COMP students',
                  solution_desc='service student can submit capstone proposals to and have feedback', approach='create a web app that allows stundets to submit proposals to',
                 num_members=3, functionalities='students submit proposals based on cirtera', technologies='flask MVC', 
                 goals='evaluate proposals from a lecturer', benefit='SWEN and COMP students', sustain='manged by lecturer eventually',
                 notes='May be revised')
    print(f'proposal created!')
    print(f'Proposal Name ' + prop.proposal_name)
    print(f'No. of Members ' + str(prop.num_members))
    print(f'Proposal ID ' + str(prop.id))
    print(f'Notes ' + prop.notes)

@rubric.command("list", help="Lists all proposals in the database")
def list_proposal_command():
    print(get_all_proposals())

app.cli.add_command(proposal) 



# Evaluation Test
# eg : flask evaluation <command>
evaluation = AppGroup('evaluation', help='Evaluation object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@evaluation.command("create", help="Creates a dummy evaluation")
@click.argument("prop", default=1)
@click.argument("notes", default="notes")
def create_evaluation_command(prop, notes):
    add_evaluation(notes, 5, 7, 5, 3, 10, 5, prop, 101)
    print(f'evaluation created!')

@evaluation.command("list", help="Lists all evaluations in the database")
def list_evaluation_command():
    print(get_all_evaluations())

app.cli.add_command(evaluation) 

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)