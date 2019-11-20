from flask import render_template, jsonify, request
from flask.views import MethodView
from ..user import User


class LoginView(MethodView):

    def get(self):
        return render_template('login.html', logininfo='')

    def post(self):
        username = request.form['username']
        password = request.form['password']
        user = User(username, password, '')
        re = user.verify_password()
        print(re)
        if re == 'ok':
            token = user.generate_token()
            print('token: ' + token)
            re_data = {'status': 'success', 'token': token}
        else:
            re_data = {'status': 'fail', 'token': ''}
        return jsonify(re_data)

        # token = request.headers.get('token')
        # print(username + ' ' + password + ' ' + token)
        # x = [{'data': 'success'}]
        # return json.dumps(x)
        # wl = "select id from t_users where user_name = '" + username + "' " + \
        #      "and password = '" + password + "'"
        # db = DB()
        # datas = db.get_data_by_sql(wl)
        # if (len(datas) != 1):
        #     print("not found user")
        #     return render_template('login.html', logininfo="*用户名或密码错误")
        # else:
        #     return redirect(url_for('api.index'))