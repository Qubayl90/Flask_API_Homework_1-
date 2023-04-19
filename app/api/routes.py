from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Cars, car_schema, cars_schema

#api = Blueprint('api',__name__, url_prefix='/api')
api = Blueprint('api',__name__, url_prefix='/api')
