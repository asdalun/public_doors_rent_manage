from flask import jsonify, request, render_template
from flask.views import MethodView
from public_doors_rent_manage.DB import DB
from public_doors_rent_manage.user import User


def get_street_and_community(username=''):
    """查询用户所在的街道和社区, 同时返回所有的街道和社区
    """
    wl = "select street, community from t_users where user_name = '" + username + "'"
    db = DB()
    re_datas, re_s = db.get_data_by_sql(wl)
    wl = "select street_name from t_streets order by street_id"
    streets, re_s = db.get_data_by_sql(wl);
    streets.insert(0, {'street_name': re_datas[0]['street']})
    wl = "select community_name from t_communities where street_name = '" + re_datas[0][
        'street'] + "' order by community_id"
    communities, re_s = db.get_data_by_sql(wl)
    communities.insert(0, {'community_name': re_datas[0]['community']})
    return streets, communities


def get_communities(street_name):
    """查询对应街道下的社区
    """
    wl = "select community_name from t_communities where street_name = '" + street_name + "' order by community_id"
    db = DB()
    re_datas, re_s = db.get_data_by_sql(wl)
    return re_datas


def change_password(user_name, old_pw, new_pw):
    """修改密码操作
    :param user_name: 用户名
    :param old_pw:    旧密码
    :param new_pw:    新密码
    :return:
    """
    params = (
        user_name,
        old_pw,
        new_pw
    )
    print('hello: ')
    print(params)
    db = DB()
    re_data, re_s = db.run_proc('change_password', params)
    if int(re_data) == 0:
        result = {'status': 'success'}
        return jsonify(result)
    elif int(re_data) == 2:
        result = {'status': 'error', 'info': '原密码输入错误！'}
        return jsonify(result)
    else:
        result = {'status': 'fail', 'info': '操作失败！' + re_s}
        return jsonify(result)


class CommonView(MethodView):
    """公共操作类
    """

    def get(self):
        opt_type = request.headers.get('opt_type')
        # 判断当前操作类型
        if opt_type == 'get_community_name':
            street_name = request.values.get('street_name', '')
            communities = get_communities(street_name)
            return jsonify({'status': 'success', 'communities': communities})
        elif opt_type == 'get_street_and_community':
            token = request.headers.get('token')
            user = User('', '', token)
            _streets = []
            _communities = []
            if user.verify_token() != 2:
                _streets, _communities = get_street_and_community(user.get_username())
            return jsonify({'status': 'success', 'streets': _streets, 'communities': _communities})
        mode = request.args.get('mode')
        # 修改密码页请求
        if mode == 'changepw':
            return render_template('changepw.html', menu3='active open', menu3_2='active')

    def post(self):
        token = request.headers.get('token')
        user = User('', '', token)
        re = user.verify_token()
        if re != 0:
            result = {'status': 'expired', 'info': '登录过期'}
            return jsonify(result)
        opt_type = request.headers.get('opt_type')
        # 修改密码操作调用
        if opt_type == 'change_password':
            return change_password(user.get_username(), request.values.get('old_pw'), request.values.get('new_pw'))
