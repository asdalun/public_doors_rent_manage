from flask import render_template, request, jsonify
from flask.views import MethodView
from public_doors_rent_manage.DB import DB
from public_doors_rent_manage.user import User
import os


class ApplyView(MethodView):
    """公租房申请页面
    """

    def get(self):
        mode = request.args.get('mode') or 'add'
        if mode == 'add':
            return render_template('apply.html', apply=None, mode=mode, menu0='active open', menu0_1='active',
                                   pagename='申请住房信息')
        elif mode == 'edit':
            apply_id = request.args.get('apply_id') or ''
            wl = "select apply_id, tenant_name, sex, tenant_IDcode, marital_status, tenant_unit, tenant_unit_address, " + \
                 "unit_pro_business, unit_pro_office, unit_pro_employment, unit_pro_retire, unit_pro_other, " + \
                 "pro_graduate, pro_outside, pro_gov_talent, pro_difficult, pro_cheap, pro_economy, card_address, " + \
                 "now_address, minimum_living_no, member_name_1, member_relation_1, member_ID_1, member_unit_1, " + \
                 "member_income_1, member_name_2, member_relation_2, member_ID_2, member_unit_2, member_income_2, " + \
                 "member_name_3, member_relation_3, member_ID_3, member_unit_3, member_income_3, member_name_4, " + \
                 "member_relation_4, member_ID_4, member_unit_4, member_income_4, member_name_5, member_relation_5, " + \
                 "member_ID_5, member_unit_5, member_income_5, income_avg, income_all, member_name_11, " + \
                 "member_address_11, member_con_area_11, member_door_pro_11, member_name_12, member_address_12, " + \
                 "member_con_area_12, member_door_pro_12, is_transfer, transfer_address_1, transfer_con_area_1, " + \
                 "is_remove, remove_address_1, remove_con_area_1, con_area_avg, user_name, transfer_pro_1, " + \
                 "remove_pro_1, convert(varchar(10), occur_date, 120) as occur_date, " + \
                 "community_name, street_name, remark " + \
                 "from t_public_doors_apply where apply_id = '" + apply_id + "'"
            db = DB()
            apply = db.get_data_by_sql(wl)
            return render_template('apply.html', apply=apply[0], mode=mode, menu0='active open', menu0_1='active',
                                   pagename='编辑申请信息')
        elif mode == 'show':
            apply_id = request.args.get('apply_id') or ''
            wl = "select apply_id, tenant_name, sex, tenant_IDcode, marital_status, tenant_unit, tenant_unit_address, " + \
                 "unit_pro_business, unit_pro_office, unit_pro_employment, unit_pro_retire, unit_pro_other, " + \
                 "pro_graduate, pro_outside, pro_gov_talent, pro_difficult, pro_cheap, pro_economy, card_address, " + \
                 "now_address, minimum_living_no, member_name_1, member_relation_1, member_ID_1, member_unit_1, " + \
                 "member_income_1, member_name_2, member_relation_2, member_ID_2, member_unit_2, member_income_2, " + \
                 "member_name_3, member_relation_3, member_ID_3, member_unit_3, member_income_3, member_name_4, " + \
                 "member_relation_4, member_ID_4, member_unit_4, member_income_4, member_name_5, member_relation_5, " + \
                 "member_ID_5, member_unit_5, member_income_5, income_avg, income_all, member_name_11, " + \
                 "member_address_11, member_con_area_11, member_door_pro_11, member_name_12, member_address_12, " + \
                 "member_con_area_12, member_door_pro_12, is_transfer, transfer_address_1, transfer_con_area_1, " + \
                 "is_remove, remove_address_1, remove_con_area_1, con_area_avg, user_name, transfer_pro_1, " + \
                 "remove_pro_1, convert(varchar(10), occur_date, 120) as occur_date, " + \
                 "community_name, street_name, remark " + \
                 "from t_public_doors_apply where apply_id = '" + apply_id + "'"
            db = DB()
            apply = db.get_data_by_sql(wl)
            return render_template('apply.html', apply=apply[0], mode=mode, menu0='active open', menu0_1='active',
                                   pagename='查看申请信息')

    def post(self):
        token = request.headers.get('token')
        user = User('', '', token)
        re = user.verify_token()
        if re != 0:
            result = {'status': 'expired', 'info': '登录过期'}
            return jsonify(result)
        sub_type = request.headers.get('sub_type')
        params = (
            request.form['_apply_id'],
            request.form['_tenant_name'],
            request.form['_tenant_IDcode'],
            request.form['_sex'],
            request.form['_marital_status'],
            request.form['_tenant_unit'],
            request.form['_tenant_unit_address'],
            request.form['_unit_pro_business'],
            request.form['_unit_pro_office'],
            request.form['_unit_pro_employment'],
            request.form['_unit_pro_retire'],
            request.form['_unit_pro_other'],
            request.form['_pro_graduate'],
            request.form['_pro_outside'],
            request.form['_pro_gov_talent'],
            request.form['_pro_difficult'],
            request.form['_pro_cheap'],
            request.form['_pro_economy'],
            request.form['_card_address'],
            request.form['_now_address'],
            request.form['_minimum_living_no'],
            request.form['_member_name_1'],
            request.form['_member_relation_1'],
            request.form['_member_ID_1'],
            request.form['_member_unit_1'],
            request.form['_member_income_1'],
            request.form['_member_name_2'],
            request.form['_member_relation_2'],
            request.form['_member_ID_2'],
            request.form['_member_unit_2'],
            request.form['_member_income_2'],
            request.form['_member_name_3'],
            request.form['_member_relation_3'],
            request.form['_member_ID_3'],
            request.form['_member_unit_3'],
            request.form['_member_income_3'],
            request.form['_member_name_4'],
            request.form['_member_relation_4'],
            request.form['_member_ID_4'],
            request.form['_member_unit_4'],
            request.form['_member_income_4'],
            request.form['_member_name_5'],
            request.form['_member_relation_5'],
            request.form['_member_ID_5'],
            request.form['_member_unit_5'],
            request.form['_member_income_5'],
            request.form['_income_avg'],
            request.form['_all_income'],
            request.form['_member_name_11'],
            request.form['_member_address_11'],
            request.form['_member_con_area_11'],
            request.form['_member_door_prop_11'],
            request.form['_member_name_12'],
            request.form['_member_address_12'],
            request.form['_member_con_area_12'],
            request.form['_member_door_prop_12'],
            request.form['_is_transfer'],
            request.form['_transfer_addres_1'],
            request.form['_transfer_con_area_1'],
            request.form['_is_remove'],
            request.form['_remove_addres_1'],
            request.form['_remove_con_area_1'],
            request.form['_con_area_avg'],
            user.get_username(),
            request.form['_occur_date'],
            request.form['_remark'],
            request.form['_street_name'],
            request.form['_community_name'],
            request.form['_transfer_pro_1'],
            request.form['_remove_pro_1'])

        db = DB()
        re_data = None
        if sub_type == 'add':
            re_data = db.run_proc('add_apply', params)
        elif sub_type == 'edit':
            re_data = db.run_proc('edit_apply', params)
        if int(re_data) == 0:
            result = {'status': 'success'}
            return jsonify(result)
        elif re_data == 2:
            result = {'status': 'repeat'}
            return jsonify(result)
        else:
            result = {'status': 'fail', 'info': 'database error'}
            return jsonify(result)
