from app.controllers.base_controller import Base
from app.blueprint import main

@main.route('/')
def base():
    return Base.base()