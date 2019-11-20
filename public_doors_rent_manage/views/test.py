from flask import render_template
from flask.views import MethodView

encoding='gb18030'


class TestView(MethodView):

    def get(self):
        # return render_template('test.html', username='dalun', menu1='active')
        print('test')
        return render_template('yulan.pdf')

    def post(selfl):
        pass