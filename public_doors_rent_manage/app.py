from flask import Flask
from public_doors_rent_manage.views import api


def create_app():
    app = Flask('public_doors_rent_manage')
    app.register_blueprint(api)
    return app
