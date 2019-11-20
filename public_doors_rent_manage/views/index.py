from flask import render_template
from flask.views import MethodView


class IndexView(MethodView):
    """系统index页面
    """
    def get(self):
        return render_template('index.html')

    def post(self):
        pass