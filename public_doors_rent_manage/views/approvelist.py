from flask import render_template, request, jsonify
from flask.views import MethodView
from public_doors_rent_manage.DB import DB
from public_doors_rent_manage.user import User


class ApproveListView(MethodView):
    """审批列表页
    """

    def get(self):
        mode = request.args.get('mode', '')
        if mode == 'street':
            wl = "select apply_id, tenant_name, tenant_unit, now_address, (street_name + '-' + community_name) as community_name, " \
                 "CONVERT(varchar(10), occur_date, 120) as occur_date, state_str, " \
                 "case when street_approve_date is NULL then '' else CONVERT(varchar(10), street_approve_date, 120) end as street_approve_date, " \
                 "case when dept_approve_date is NULL then '' else CONVERT(varchar(10), dept_approve_date, 120) end as dept_approve_date, " \
                 "street_approve_remark, dept_approve_remark from v_public_doors_apply " + \
                 "order by occur_date desc"
            db = DB()
            re_datas, re_s = db.get_data_by_sql(wl)
            if re_s == '':
                return render_template('approvelist.html', menu1='active open', menu1_2='active', pagename='街道审批信息查询',
                                    mode='street', applylist=re_datas)
            else:
                return render_template('error.html', errorinfo=re_s)
        elif mode == 'streetsearch':
            s_date = request.args.get('s_date', '')
            e_date = request.args.get('e_date', '')
            wl = "select apply_id, tenant_name, tenant_unit, now_address, (street_name + '-' + community_name) as community_name, " \
                 "CONVERT(varchar(10), occur_date, 120) as occur_date, state_str, " \
                 "case when street_approve_date is NULL then '' else CONVERT(varchar(10), street_approve_date, 120) end as street_approve_date, " \
                 "case when dept_approve_date is NULL then '' else CONVERT(varchar(10), dept_approve_date, 120) end as dept_approve_date, " \
                 "street_approve_remark, dept_approve_remark from v_public_doors_apply " \
                 "where CONVERT(varchar(10), street_approve_date, 120) >= '" + s_date + "' " \
                 "and CONVERT(varchar(10), street_approve_date, 120) <= '" + e_date + "' " \
                 "order by occur_date desc"
            db = DB()
            re_datas, re_s = db.get_data_by_sql(wl)
            if re_s == '':
                return render_template('approvelist.html', menu1='active open', menu1_2='active', pagename='街道审批信息查询',
                                       mode='street', applylist=re_datas)
            else:
                return render_template('error.html', errorinfo=re_s)
        elif mode == 'dept':
            wl = "select apply_id, tenant_name, tenant_unit, now_address, (street_name + '-' + community_name) as community_name, " \
                 "CONVERT(varchar(10), occur_date, 120) as occur_date, state_str, " \
                 "case when street_approve_date is NULL then '' else CONVERT(varchar(10), street_approve_date, 120) end as street_approve_date, " \
                 "case when dept_approve_date is NULL then '' else CONVERT(varchar(10), dept_approve_date, 120) end as dept_approve_date, " \
                 "street_approve_remark, dept_approve_remark from v_public_doors_apply " + \
                 "order by occur_date desc"
            db = DB()
            re_datas, re_s = db.get_data_by_sql(wl)
            if re_s == '':
                return render_template('approvelist.html', menu1='active open', menu1_4='active', pagename='局审批信息查询',
                                       mode='dept', applylist=re_datas)
            else:
                return render_template('error.html', errorinfo=re_s)
        elif mode == 'deptsearch':
            s_date = request.args.get('s_date', '')
            e_date = request.args.get('e_date', '')
            wl = "select apply_id, tenant_name, tenant_unit, now_address, (street_name + '-' + community_name) as community_name, " \
                 "CONVERT(varchar(10), occur_date, 120) as occur_date, state_str, " \
                 "case when street_approve_date is NULL then '' else CONVERT(varchar(10), street_approve_date, 120) end as street_approve_date, " \
                 "case when dept_approve_date is NULL then '' else CONVERT(varchar(10), dept_approve_date, 120) end as dept_approve_date, " \
                 "street_approve_remark, dept_approve_remark from v_public_doors_apply " \
                 "where CONVERT(varchar(10), dept_approve_date, 120) >= '" + s_date + "' " \
                 "and CONVERT(varchar(10), dept_approve_date, 120) <= '" + e_date + "' " \
                 "order by occur_date desc"
            db = DB()
            re_datas, re_s = db.get_data_by_sql(wl)
            if re_s == '':
                return render_template('approvelist.html', menu1='active open', menu1_4='active', pagename='局审批信息查询',
                                       mode='dept', applylist=re_datas)
            else:
                return render_template('error.html', errorinfo=re_s)

    def post(self):
        pass