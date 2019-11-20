from flask import Blueprint
from public_doors_rent_manage.views.test import TestView
from public_doors_rent_manage.views.login import LoginView
from public_doors_rent_manage.views.index import IndexView
from public_doors_rent_manage.views.token import TokenView
from public_doors_rent_manage.views.apply import ApplyView
from public_doors_rent_manage.views.applylist import ApplyListView
from public_doors_rent_manage.views.common import CommonView
from public_doors_rent_manage.views.reports import ReportView
from public_doors_rent_manage.views.approve import ApproveView
from public_doors_rent_manage.views.approvelist import ApproveListView

api = Blueprint('api', __name__)
api.add_url_rule('/test', view_func=TestView.as_view('test'))
api.add_url_rule('/index', view_func=IndexView.as_view('index'))
api.add_url_rule('/login', view_func=LoginView.as_view('login'))
api.add_url_rule('/token', view_func=TokenView.as_view('token'))
api.add_url_rule('/apply', view_func=ApplyView.as_view('apply'))
api.add_url_rule('/applylist', view_func=ApplyListView.as_view('applylist'))
api.add_url_rule('/common', view_func=CommonView.as_view('common'))
api.add_url_rule('/reports', view_func=ReportView.as_view('report'))
api.add_url_rule('/approve', view_func=ApproveView.as_view('approve'))
api.add_url_rule('/approvelist', view_func=ApproveListView.as_view('approvelist'))

