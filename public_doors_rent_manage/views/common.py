from flask import jsonify, request
from flask.views import MethodView
from public_doors_rent_manage.DB import DB
from public_doors_rent_manage.user import User


def get_street_and_community(username=''):
    """查询用户所在的街道和社区, 同时返回所有的街道和社区
    """
    wl = "select street, community from t_users where user_name = '" + username + "'"
    db = DB()
    res = db.get_data_by_sql(wl)
    wl = "select street_name from t_streets order by street_id"
    streets = db.get_data_by_sql(wl);
    streets.insert(0, {'street_name': res[0]['street']})
    wl = "select community_name from t_communities where street_name = '" + res[0]['street'] + "' order by community_id"
    communities = db.get_data_by_sql(wl)
    communities.insert(0, {'community_name': res[0]['community']})
    return streets, communities


def get_communities(street_name):
    """查询对应街道下的社区
    """
    wl = "select community_name from t_communities where street_name = '" + street_name + "' order by community_id"
    db = DB()
    return db.get_data_by_sql(wl)


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
