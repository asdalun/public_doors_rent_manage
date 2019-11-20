from flask import request, jsonify
from flask.views import MethodView
from public_doors_rent_manage.user import User


class TokenView(MethodView):

    def get(self):
        token = request.headers.get('token')
        user = User('', '', token)
        re = user.verify_token()
        # print('the re is: ' + str(re))
        if re == 0:
            return jsonify({'status': 'ok', 'token': '', 'username': user.get_username()})
        elif re == 1:
            token = user.generate_token()
            print('the new token: ' + token)
            return jsonify({'status': 'refresh_token', 'token': token, 'username': user.get_username()})
        else:
            return jsonify({'status': 'expired', 'token': '', 'username': 'error'})

    def post(self):
        token = request.headers.get('token')
        username = request.values.get('username', '')
        print('post usename is: ' + username)
        user = User(username, '', token)
        re = user.verify_token()
        print('the re is: ' + str(re))
        if re == 0:
            return jsonify({'status': 'ok', 'token': '', 'username': user.get_username()})
        elif re == 1:
            token = user.generate_token()
            print('the new token: ' + token)
            return jsonify({'status': 'refresh_token', 'token': token, 'username': user.get_username()})
        else:
            return jsonify({'status': 'expired', 'token': '', 'username': 'error'})