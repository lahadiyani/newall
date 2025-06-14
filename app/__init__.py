from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    from app.routes.base_route import main
    app.register_blueprint(main)
    CORS(app)
    return app