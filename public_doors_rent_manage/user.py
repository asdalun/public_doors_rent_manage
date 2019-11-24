from public_doors_rent_manage.DB import DB
from datetime import datetime, timedelta
from flask import current_app
from calendar import timegm
import jwt


class User:
    """用户操作类，用于生成用户，验证用户，Token等操作
    """
    def __init__(self, _username, _password, _token):
        self._username = _username
        self._password = _password
        self._usersort = ''
        self._dept = ''
        self._token = _token

    def verify_password(self):
        """
        验证用户名密码是否正确
        :return: 正确返回 ok，错误返回error
        """
        wl = "select id, user_sort, dept from t_users where user_name = '" + self._username + "' " + \
             "and password = '" + self._password + "'"
        db = DB()
        re_datas, re_s = db.get_data_by_sql(wl)
        if re_datas is None:
            return re_s
        else:
            if len(re_datas) != 1:
                self._username = ''
                self._password = ''
                self._dept = ''
                return 'error'
            else:
                self._usersort = re_datas[0]['user_sort']
                self._dept = re_datas[0]['dept']
                return 'ok'

    def generate_token(self):
        """
        生成token，有效期为1天，过期10分钟可以使用老的token刷新获得新的token
        :return: 返回生成的token
        """
        if self._username == '':
            return 'not login'
        # 过期时间
        exp = datetime.now() + timedelta(minutes=120)
        print(exp.strftime('%Y-%m-%d %H:%M:%S'))
        # token 过期后十分钟内，还可以使用老 token 进行刷新 token
        refresh_exp = timegm((exp + timedelta(seconds=600)).timetuple())
        # refresh_exp_str = refresh_exp.strftime('%Y-%m-%d %H:%M:%S')
        payload = {
            'username': self._username,
            'usersort': self._usersort,
            'dept': self._dept,
            'exp': exp,
            'refresh_exp': refresh_exp
        }
        print(payload)
        return jwt.encode(payload, current_app.secret_key, algorithm='HS512').decode('utf-8')

    def verify_token(self, verify_exp=True):
        """
        验证token是否在有效期之内
        :param verify_exp: 是否验证token过期时间
        :return: 有效返回 0；在刷新时间之内返回 1；失效返回 2；
        """
        if self._token == '':
            return 2
        if verify_exp:
            options = {'verify_exp': True}
        else:
            options = {'verify_exp': False}
        try:
            payload = jwt.decode(self._token, current_app.secret_key, verify=True,
                                 algorithms='HS512', options=options,
                                 require_exp=True)
            print(payload)
        except jwt.InvalidTokenError as ex:
            print('the error is: ' + str(ex))
            return 2
        if any(('usersort' not in payload, 'username' not in payload, 'dept' not in payload,
                'refresh_exp' not in payload, 'exp' not in payload)):
            return 2
        now = datetime.now()
        # token在验证期内
        if timegm(now.timetuple()) <= payload['exp']:
            self._username = payload['username']
            self._dept = payload['dept']
            return 0
        elif payload['exp'] < timegm(now.timetuple()) <= payload['refresh_exp']:
            self._username = payload['username']
            self._dept = payload['dept']
            return 1
        else:
            return 2

    def get_username(self):
        return self._username

    def get_community(self):
        """
        查询登录用户的社区，并返回
        :return: 社区名称
        """
        wl = "select community from t_users where user_name = '" + self._username + "'"
        db = DB()
        re_datas, re_s = db.get_data_by_sql(wl)
        if len(re_datas) != 1:
            return ''
        else:
            return re_datas[0]['community']

    def get_street(self):
        """
        查询登录用户的街道，并返回
        :return: 街道名称
        """
        wl = "select street from t_users where user_name = '" + self._username + "'"
        db = DB()
        re_datas, re_s = db.get_data_by_sql(wl)
        if len(re_datas) != 1:
            return ''
        else:
            return re_datas[0]['street']





