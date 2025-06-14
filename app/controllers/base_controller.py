from flask import render_template

class Base:
    @staticmethod
    def base():
        return render_template('index.html')