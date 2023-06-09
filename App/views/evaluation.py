from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required
from App.controllers import student_required, lecturer_required

from.index import index_views

evaluation_views = Blueprint('evaluation_views', __name__, template_folder='../templates')

#@student_required
@evaluation_views.route('/proposal-evaluation', methods=['GET'])
def get_evaluation_page():
    return render_template('evaluation.html')


