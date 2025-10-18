from flask import Flask
from flask_migrate import Migrate
from db import db

def create_app():
    app = Flask(__name__, template_folder='template')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/ninicui/Documents/flask/dbapplication/testdb.db'

    db.init_app(app)

    from routes import register_route
    register_route(app)

    migrate = Migrate(app, db)
     
    return app

if __name__ == '__main__':
    create_app().run(host='0.0.0.0', port=5001, debug=True)
