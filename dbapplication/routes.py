from models import Person
from db import db
from flask import request

def register_route(app):

    @app.route('/')
    def index():
        people = Person.query.all()
        return str(people)
    
    @app.route('/add_user', methods=['GET', 'POST'])
    def add_user():
        # name = request.json["name"]
        # age = request.json["age"]
        name = request.args.get('name')
        age = request.args.get('age')
        new_user = Person(name=name, age=age)
        db.session.add(new_user)
        db.session.commit()
        return f'User {name} is inserted successfully'