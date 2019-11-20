from flask import render_template, request, jsonify
from flask.views import MethodView
from public_doors_rent_manage.DB import DB
from public_doors_rent_manage.user import User


class ApproveView(MethodView):
    """审批页视图
    """

    def get(self):
        mode = request.args.get('mode', '');
        apply_id = request.args.get('apply_id', '');
        wl = "select apply_id, tenant_name, sex, tenant_IDcode, marital_status, tenant_unit, tenant_unit_address, " + \
             "unit_property, unit_pro_business, unit_pro_office, unit_pro_employment, unit_pro_retire, unit_pro_other, " + \
             "pro_graduate, pro_outside, pro_gov_talent, pro_difficult, pro_cheap, pro_economy, card_address, " + \
             "now_address, minimum_living_no, member_name_1, member_relation_1, member_ID_1, member_unit_1, " + \
             "member_income_1, member_name_2, member_relation_2, member_ID_2, member_unit_2, member_income_2, " + \
             "member_name_3, member_relation_3, member_ID_3, member_unit_3, member_income_3, member_name_4, " + \
             "member_relation_4, member_ID_4, member_unit_4, member_income_4, member_name_5, member_relation_5, " + \
             "member_ID_5, member_unit_5, member_income_5, income_avg, income_all, member_name_11, member_address_11, " + \
             "member_con_area_11, member_door_pro_11, member_name_12, member_address_12, member_con_area_12, " + \
             "member_door_pro_12, is_transfer, transfer_address_1, transfer_con_area_1, is_remove, remove_address_1, " + \
             "remove_con_area_1, con_area_avg, user_name, occur_date, community_name, street_name, remark, " + \
             "transfer_pro_1, remove_pro_1, state_str " + \
             "FROM v_public_doors_apply where apply_id = '" + apply_id + "'"
        db = DB()
        re_datas = db.get_data_by_sql(wl)
        if len(re_datas) != 1:
            apply = None
        else:
            apply = re_datas[0]
        if mode == 'search' or mode == '':
            return render_template('approve.html', apply=apply, menu0='active open', menu0_3='active', mode='search',
                                   pagename='公租房申请审批表查询')
        elif mode == 'street':
            return render_template('approve.html', apply=apply, menu1='active open', menu1_1='active', mode='street',
                                   pagename='公租房申请街道审批')
        elif mode == 'dept':
            return render_template('approve.html', apply=apply, menu1='active open', menu1_1='active', mode='dept',
                                   pagename='公租房申请局审批')

    def post(self):
        token = request.headers.get('token')
        user = User('', '', token)
        re = user.verify_token()
        if re != 0:
            result = {'status': 'expired', 'info': '登录过期'}
            return jsonify(result)
        opt_type = request.headers.get('opt_type')
        if opt_type == 'street_approve':
            params = (
                request.values.get('apply_id'),
                request.values.get('street_approve_remark'),
                user.get_username()
            )
            db = DB()
            re_data = None
            re_data = db.run_proc('approve_street', params)
            if int(re_data) == 0:
                result = {'status': 'success'}
                return jsonify(result)
            elif int(re_data) == 1:
                result = {'status': 'state', 'info': '该表单不在 未审批 状态！'}
                return jsonify(result)
            elif int(re_data) == 2:
                result = {'status': 'street', 'info': '不在同一街道，无法审批！'}
                return jsonify(result)
            else:
                result = {'status': 'fail', 'info': '审批失败！'}
                return jsonify(result)
        elif opt_type == 'dept_approve':
            params = (
                request.values.get('apply_id'),
                request.values.get('dept_approve_remark'),
                user.get_username()
            )
            db = DB()
            re_data = None
            re_data = db.run_proc('approve_dept', params)
            if int(re_data) == 0:
                result = {'status': 'success'}
                return jsonify(result)
            elif int(re_data) == 1:
                result = {'status': 'state', 'info': '该表单不在 街道已审批 状态！'}
                return jsonify(result)
            else:
                result = {'status': 'fail', 'info': '审批失败！'}
                return jsonify(result)
