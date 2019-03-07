from flask import Flask

from toy_box.database import init_db

def create_app():
    app = Flask(__name__)
    app.config.from_object('toy_box.config.Config')

    init_db(app)

    return app

app = create_app()

