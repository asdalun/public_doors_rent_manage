from flask import render_template, request, jsonify
from flask.views import MethodView
from public_doors_rent_manage.DB import DB
from public_doors_rent_manage.user import User


class ApplyListView(MethodView):
    """申请住房信息列表
    """
    def get(self):
        mode = request.args.get('mode') or ''
        if mode == '':
            wl = "select apply_id, tenant_name, tenant_unit, now_address, (street_name + '-' + community_name) as community_name, " + \
                 "CONVERT(varchar(10), occur_date, 120) as occur_date, state_str, remark from v_public_doors_apply " + \
                 "order by occur_date"
            db = DB()
            applylist = db.get_data_by_sql(wl)
            return render_template('applylist.html', menu0='active open', menu0_2='active', pagename='申请信息列表',
                                   applylist=applylist)
        elif mode == 'search':
            s_date = request.args.get('s_date')
            e_date = request.args.get('e_date')
            wl = "select apply_id, tenant_name, tenant_unit, now_address, (street_name + '-' + community_name) as community_name, " + \
                 "CONVERT(varchar(10), occur_date, 120) as occur_date, state_str, remark from v_public_doors_apply " + \
                 "where CONVERT(varchar(10), occur_date, 120) >= '" + s_date + "' and " + \
                 "CONVERT(varchar(10), occur_date, 120) <= '" + e_date + "' " + \
                 "order by occur_date"
            db = DB()
            print(wl)
            applylist = db.get_data_by_sql(wl)
            return render_template('applylist.html', menu0='active open', menu0_2='active', pagename='申请信息列表',
                                   applylist=applylist)

    def post(self):
        token = request.headers.get('token')
        user = User('', '', token)
        re = user.verify_token()
        if re != 0:
            result = {'status': 'expired', 'info': '登录过期'}
            return jsonify(result)
        params = (request.values.get('apply_id', ''))
        db = DB()
        re_data = db.run_proc('del_apply', params)
        if re_data == 0:
            return jsonify({'status': 'success'})
        elif re_data == 2:
            return jsonify({'status': 'approve'})
        else:
            return jsonify({'status': 'fail', 'info': '删除申请信息失败！'})