from flask import render_template, request, jsonify
from flask.views import MethodView
from public_doors_rent_manage.user import User
from public_doors_rent_manage.DB import DB
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.charts.lineplots import Line
from reportlab.graphics.shapes import Drawing, Rect
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

# 系统主目录
main_path = 'public_doors_rent_manage/'
# pdf文件所在目录
report_path = 'static/reports/'


def get_label(x, y, text, size):
    label = Label(x=x, y=y, fontName='simsun', fontSize=size)
    label.setText(text)
    return label


def get_apply_table(apply_id):
    """
    生成申请审批表
    :param apply_id: 审批表编号
    :return: 生成的pdf路径
    """
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
         "transfer_pro_1, remove_pro_1 " + \
         "FROM t_public_doors_apply where apply_id = '" + apply_id + "'"
    db = DB()
    apply = db.get_data_by_sql(wl)
    if len(apply) == 0:
        return 'not found'
    pdfmetrics.registerFont(TTFont('simsun', 'SimSun.ttf'))
    pdfmetrics.registerFont(TTFont('simhei', 'SimHei.ttf'))
    style_sheet = getSampleStyleSheet()
    # 标题
    title_style = style_sheet['Title']
    title_style.fontName = 'simhei'
    title_style.fontSize = 22
    elements = [Paragraph('立山区公共租赁租房（申请）审批表', title_style)]
    elements.append(Spacer(0, 0.3 * cm))
    # 标题下一行小字
    doc_style = ParagraphStyle(name='rightstyle', fontName='simsun', fontSize=10, alignment=TA_CENTER)
    line0 = Paragraph('编号：' + apply_id + '\0' * 30 + '单位：平方米，人，元', doc_style)
    elements.append(line0)
    elements.append(Spacer(0, 0.3 * cm))
    # 创建画布，画表格
    width, height = 19 * cm, 25 * cm;
    # 第一页开画
    d1 = Drawing(width, height)
    d1.background = Rect(0, 0, width, height, strokeWidth=1, strokeColor="#000000", fillColor=None)  # 边框颜色
    d1.add(Line(1.2 * cm, 24 * cm, width, 24 * cm, strokeWidth=0.5))
    d1.add(Line(1.2 * cm, 23 * cm, width, 23 * cm, strokeWidth=0.5))
    d1.add(Line(1.2 * cm, 22 * cm, width, 22 * cm, strokeWidth=0.5))
    d1.add(Line(1.2 * cm, 21 * cm, width, 21 * cm, strokeWidth=0.5))
    d1.add(Line(1.2 * cm, 19.5 * cm, width, 19.5 * cm, strokeWidth=0.5))
    d1.add(Line(1.2 * cm, 18 * cm, width, 18 * cm, strokeWidth=0.5))
    d1.add(Line(1.2 * cm, 17 * cm, width, 17 * cm, strokeWidth=0.5))
    d1.add(Line(0 * cm, 16 * cm, width, 16 * cm, strokeWidth=0.8))
    d1.add(Line(1.2 * cm, 25 * cm, 1.2 * cm, 8.8 * cm, strokeWidth=0.5))
    d1.add(Line(3.5 * cm, 25 * cm, 3.5 * cm, 0 * cm, strokeWidth=0.5))
    d1.add(Line(6.5 * cm, 25 * cm, 6.5 * cm, 24 * cm, strokeWidth=0.5))
    d1.add(Line(8.0 * cm, 25 * cm, 8.0 * cm, 24 * cm, strokeWidth=0.5))
    d1.add(Line(10 * cm, 25 * cm, 10 * cm, 24 * cm, strokeWidth=0.5))
    d1.add(Line(12 * cm, 25 * cm, 12 * cm, 24 * cm, strokeWidth=0.5))
    d1.add(Line(10 * cm, 23 * cm, 10 * cm, 22 * cm, strokeWidth=0.5))
    d1.add(Line(12 * cm, 23 * cm, 12 * cm, 22 * cm, strokeWidth=0.5))
    d1.add(get_label(x=2.25 * cm, y=24.5 * cm, text='姓名', size=10))
    d1.add(get_label(x=5 * cm, y=24.5 * cm, text=apply[0]['tenant_name'], size=10))
    d1.add(get_label(x=7.25 * cm, y=24.5 * cm, text='性别', size=10))
    d1.add(get_label(x=9 * cm, y=24.5 * cm, text=apply[0]['sex'], size=10))
    d1.add(get_label(x=11 * cm, y=24.5 * cm, text='身份证', size=10))
    d1.add(get_label(x=14.5 * cm, y=24.5 * cm, text=apply[0]['tenant_IDcode'], size=10))
    d1.add(get_label(x=2.25 * cm, y=23.5 * cm, text='婚姻状况', size=10))
    d1.add(get_label(x=4.5 * cm, y=23.5 * cm, text=apply[0]['marital_status'], size=10))
    d1.add(get_label(x=2.25 * cm, y=22.5 * cm, text='工作单位', size=10))
    d1.add(get_label(x=6.5 * cm, y=22.5 * cm, text=apply[0]['tenant_unit'], size=10))
    d1.add(get_label(x=11 * cm, y=22.5 * cm, text='单位地址', size=10))
    d1.add(get_label(x=15.5 * cm, y=22.5 * cm, text=apply[0]['tenant_unit_address'], size=10))
    d1.add(get_label(x=2.25 * cm, y=21.5 * cm, text='单位性质', size=10))
    unit_pro = ''
    if int(apply[0]['unit_pro_business']) == 1:
        unit_pro += '企业 '
    if int(apply[0]['unit_pro_office']) == 1:
        unit_pro += '机关 '
    if int(apply[0]['unit_pro_employment']) == 1:
        unit_pro += '个体 '
    if int(apply[0]['unit_pro_retire']) == 1:
        unit_pro += '退休 '
    if int(apply[0]['unit_pro_other']) == 1:
        unit_pro += '其它'
    d1.add(get_label(x=10 * cm, y=21.5 * cm, text=unit_pro, size=10))
    d1.add(get_label(x=2.25 * cm, y=20.25 * cm, text='申请人类型', size=10))
    tenant_pro = ''
    if int(apply[0]['pro_graduate']) == 1:
        tenant_pro += '新就业普通高校毕业生'
    if int(apply[0]['pro_outside']) == 1:
        tenant_pro += '外来务工人员'
    if int(apply[0]['pro_gov_talent']) == 1:
        tenant_pro += '政府引进特殊人才'
    if int(apply[0]['pro_difficult']) == 1:
        tenant_pro += '困难家庭'
    if int(apply[0]['pro_cheap']) == 1:
        tenant_pro += '廉租房保障家庭'
    if int(apply[0]['pro_economy']) == 1:
        tenant_pro += '经济房保障家庭'
    d1.add(get_label(x=10 * cm, y=20.25 * cm, text=tenant_pro, size=10))
    d1.add(get_label(x=2.25 * cm, y=18.75 * cm, text='户口所在\n\0地址', size=10))
    d1.add(get_label(x=10 * cm, y=18.75 * cm, text=apply[0]['card_address'], size=10))
    d1.add(get_label(x=2.25 * cm, y=17.5 * cm, text='现居住地址', size=10))
    d1.add(get_label(x=10 * cm, y=17.5 * cm, text=apply[0]['now_address'], size=10))
    d1.add(get_label(x=2.25 * cm, y=16.5 * cm, text='低保证号', size=10))
    d1.add(get_label(x=10 * cm, y=16.5 * cm, text=apply[0]['minimum_living_no'], size=10))
    d1.add(get_label(x=0.5 * cm, y=20.5 * cm, text='申\n请\n人\n基\n本\n情\n况\n及\n申\n请\n公\n共\n租\n赁\n住\n房\n情\n况', size=10))
    d1.add(Line(1.2 * cm, 14.8 * cm, width, 14.8 * cm, strokeWidth=0.5))
    d1.add(Line(1.2 * cm, 13.6 * cm, width, 13.6 * cm, strokeWidth=0.5))
    d1.add(Line(1.2 * cm, 12.4 * cm, width, 12.4 * cm, strokeWidth=0.5))
    d1.add(Line(1.2 * cm, 11.2 * cm, width, 11.2 * cm, strokeWidth=0.5))
    d1.add(Line(1.2 * cm, 10 * cm, width, 10 * cm, strokeWidth=0.5))
    d1.add(Line(0 * cm, 8.8 * cm, width, 8.8 * cm, strokeWidth=0.8))
    d1.add(Line(6 * cm, 16 * cm, 6 * cm, 8.8 * cm, strokeWidth=0.5))
    d1.add(Line(11 * cm, 16 * cm, 11 * cm, 7.3 * cm, strokeWidth=0.5))
    d1.add(Line(16.5 * cm, 16 * cm, 16.5 * cm, 8.8 * cm, strokeWidth=0.5))
    d1.add(Line(0 * cm, 7.3 * cm, width, 7.3 * cm, strokeWidth=0.8))
    d1.add(Line(13.5 * cm, 8.8 * cm, 13.5 * cm, 7.3 * cm, strokeWidth=0.5))
    d1.add(get_label(x=0.5 * cm, y=12.5 * cm, text='申\n请\n人\n家\n庭\n收\n入\n情\n况', size=10))
    d1.add(get_label(x=2.25 * cm, y=15.4 * cm, text='与申请\n人关系', size=10))
    d1.add(get_label(x=2.25 * cm, y=14.2 * cm, text=apply[0]['member_relation_1'], size=10))
    d1.add(get_label(x=2.25 * cm, y=13 * cm, text=apply[0]['member_relation_2'], size=10))
    d1.add(get_label(x=2.25 * cm, y=11.8 * cm, text=apply[0]['member_relation_3'], size=10))
    d1.add(get_label(x=2.25 * cm, y=10.6 * cm, text=apply[0]['member_relation_4'], size=10))
    d1.add(get_label(x=2.25 * cm, y=9.4 * cm, text=apply[0]['member_relation_5'], size=10))
    d1.add(get_label(x=4.75 * cm, y=15.4 * cm, text='姓名', size=10))
    d1.add(get_label(x=4.75 * cm, y=14.2 * cm, text=apply[0]['member_name_1'], size=10))
    d1.add(get_label(x=4.75 * cm, y=13 * cm, text=apply[0]['member_name_2'], size=10))
    d1.add(get_label(x=4.75 * cm, y=11.8 * cm, text=apply[0]['member_name_3'], size=10))
    d1.add(get_label(x=4.75 * cm, y=10.6 * cm, text=apply[0]['member_name_4'], size=10))
    d1.add(get_label(x=4.75 * cm, y=9.4 * cm, text=apply[0]['member_name_5'], size=10))
    d1.add(get_label(x=8.5 * cm, y=15.4 * cm, text='身份证', size=10))
    d1.add(get_label(x=8.5 * cm, y=14.2 * cm, text=apply[0]['member_ID_1'], size=10))
    d1.add(get_label(x=8.5 * cm, y=13 * cm, text=apply[0]['member_ID_2'], size=10))
    d1.add(get_label(x=8.5 * cm, y=11.8 * cm, text=apply[0]['member_ID_3'], size=10))
    d1.add(get_label(x=8.5 * cm, y=10.6 * cm, text=apply[0]['member_ID_4'], size=10))
    d1.add(get_label(x=8.5 * cm, y=9.4 * cm, text=apply[0]['member_ID_5'], size=10))
    d1.add(get_label(x=13.75 * cm, y=15.4 * cm, text='工作单位', size=10))
    d1.add(get_label(x=13.75 * cm, y=14.2 * cm, text=apply[0]['member_unit_1'], size=10))
    d1.add(get_label(x=13.75 * cm, y=13 * cm, text=apply[0]['member_unit_2'], size=10))
    d1.add(get_label(x=13.75 * cm, y=11.8 * cm, text=apply[0]['member_unit_3'], size=10))
    d1.add(get_label(x=13.75 * cm, y=10.6 * cm, text=apply[0]['member_unit_4'], size=10))
    d1.add(get_label(x=13.75 * cm, y=9.4 * cm, text=apply[0]['member_unit_5'], size=10))
    d1.add(get_label(x=17.75 * cm, y=15.4 * cm, text='年收入', size=10))
    d1.add(get_label(x=17.75 * cm, y=14.2 * cm, text=str(apply[0]['member_income_1']), size=10))
    d1.add(get_label(x=17.75 * cm, y=13 * cm, text=str(apply[0]['member_income_2']), size=10))
    d1.add(get_label(x=17.75 * cm, y=11.8 * cm, text=str(apply[0]['member_income_3']), size=10))
    d1.add(get_label(x=17.75 * cm, y=10.6 * cm, text=str(apply[0]['member_income_4']), size=10))
    d1.add(get_label(x=17.75 * cm, y=9.4 * cm, text=str(apply[0]['member_income_5']), size=10))
    d1.add(get_label(x=1.8 * cm, y=8.1 * cm, text='家庭人均月收入', size=10))
    d1.add(get_label(x=4.8 * cm, y=8.1 * cm, text=str(apply[0]['income_avg']), size=10))
    d1.add(get_label(x=12.25 * cm, y=8.1 * cm, text='家庭成员\n年收入合计', size=10))
    d1.add(get_label(x=14.5 * cm, y=8.1 * cm, text=str(apply[0]['income_all']), size=10))
    d1.add(get_label(x=1.8 * cm, y=4.1 * cm, text='家庭收入\n认定意见', size=10))
    d1.add(get_label(x=11.8 * cm, y=4.1 * cm, text='经办人', size=10))
    d1.add(get_label(x=15.8 * cm, y=4.1 * cm, text='认定部门（盖章）', size=10))
    d1.add(get_label(x=15.8 * cm, y=1.1 * cm, text='年\0\0\0月\0\0\0日', size=10))
    elements.append(d1)
    # 第二页 开画
    d2 = Drawing(width, height)
    d2.background = Rect(0, 0, width, height, strokeWidth=1, strokeColor="#000000", fillColor=None)  # 边框颜色
    d2.add(Line(1.2 * cm, 25 * cm, 1.2 * cm, 17.5 * cm, strokeWidth=0.5))
    d2.add(Line(1.2 * cm, 23.5 * cm, width, 23.5 * cm, strokeWidth=0.5))
    d2.add(Line(1.2 * cm, 22 * cm, width, 22 * cm, strokeWidth=0.5))
    d2.add(Line(1.2 * cm, 20.5 * cm, width, 20.5 * cm, strokeWidth=0.5))
    d2.add(Line(1.2 * cm, 19 * cm, width, 19 * cm, strokeWidth=0.5))
    d2.add(Line(0 * cm, 17.5 * cm, width, 17.5 * cm, strokeWidth=0.5))
    d2.add(Line(0 * cm, 16 * cm, width, 16 * cm, strokeWidth=0.8))
    d2.add(Line(5.2 * cm, 25 * cm, 5.2 * cm, 16 * cm, strokeWidth=0.5))
    d2.add(Line(13.2 * cm, 25 * cm, 13.2 * cm, 17.5 * cm, strokeWidth=0.5))
    d2.add(Line(16.2 * cm, 25 * cm, 16.2 * cm, 17.5 * cm, strokeWidth=0.5))
    d2.add(Line(0 * cm, 11 * cm, width, 11 * cm, strokeWidth=0.8))
    d2.add(Line(0 * cm, 6 * cm, width, 6 * cm, strokeWidth=0.8))
    d2.add(Line(9.5 * cm, 16 * cm, 9.5 * cm, 11 * cm, strokeWidth=0.8))
    d2.add(get_label(x=0.5 * cm, y=21.5 * cm, text='申\n请\n人\n家\n庭\n成\n员\n住\n房\n情\n况', size=10))
    d2.add(get_label(x=3.25 * cm, y=24.2 * cm, text='产权人或承租人', size=10))
    d2.add(get_label(x=3.25 * cm, y=22.8 * cm, text=apply[0]['member_name_11'], size=10))
    d2.add(get_label(x=3.25 * cm, y=21.2 * cm, text=apply[0]['member_name_12'], size=10))
    d2.add(get_label(x=9.25 * cm, y=24.2 * cm, text='房屋坐落', size=10))
    d2.add(get_label(x=9.25 * cm, y=22.8 * cm, text=apply[0]['member_address_11'], size=10))
    d2.add(get_label(x=9.25 * cm, y=21.2 * cm, text=apply[0]['member_address_12'], size=10))
    d2.add(get_label(x=14.75 * cm, y=24.2 * cm, text='建筑面积', size=10))
    d2.add(get_label(x=14.75 * cm, y=22.8 * cm, text=str(apply[0]['member_con_area_11']), size=10))
    d2.add(get_label(x=14.75 * cm, y=21.2 * cm, text=str(apply[0]['member_con_area_12']), size=10))
    d2.add(get_label(x=17.55 * cm, y=24.2 * cm, text='住房性质', size=10))
    d2.add(get_label(x=17.55 * cm, y=22.8 * cm, text=apply[0]['member_door_pro_11'], size=10))
    d2.add(get_label(x=17.55 * cm, y=21.2 * cm, text=apply[0]['member_door_pro_12'], size=10))
    d2.add(get_label(x=3.25 * cm, y=19.75 * cm, text='近五年转让\n房屋情况', size=10))
    d2.add(get_label(x=9.25 * cm, y=19.75 * cm, text=apply[0]['transfer_address_1'], size=10))
    d2.add(get_label(x=14.75 * cm, y=19.75 * cm, text=str(apply[0]['transfer_con_area_1']), size=10))
    d2.add(get_label(x=17.55 * cm, y=19.75 * cm, text=str(apply[0]['transfer_pro_1']), size=10))
    d2.add(get_label(x=3.25 * cm, y=18.25 * cm, text='近五年拆迁\n房屋情况', size=10))
    d2.add(get_label(x=9.25 * cm, y=18.25 * cm, text=apply[0]['remove_address_1'], size=10))
    d2.add(get_label(x=14.75 * cm, y=18.25 * cm, text=str(apply[0]['remove_con_area_1']), size=10))
    d2.add(get_label(x=17.55 * cm, y=18.25 * cm, text=str(apply[0]['remove_pro_1']), size=10))
    d2.add(get_label(x=2.25 * cm, y=16.75 * cm, text='家庭人均建筑面积', size=10))
    d2.add(get_label(x=9.25 * cm, y=16.75 * cm, text=str(apply[0]['con_area_avg']), size=10))
    d2.add(get_label(x=2 * cm, y=15.25 * cm, text='所在社区意见：', size=10))
    d2.add(get_label(x=1.45 * cm, y=13.5 * cm, text='负责人：', size=10))
    d2.add(get_label(x=1.45 * cm, y=12.5 * cm, text='经办人：', size=10))
    d2.add(get_label(x=7.45 * cm, y=12.5 * cm, text='公章', size=10))
    d2.add(get_label(x=7.45 * cm, y=11.5 * cm, text='年\0\0\0月\0\0\0日', size=10))
    d2.add(get_label(x=11.9 * cm, y=15.25 * cm, text='所在街道办事处意见：', size=10))
    d2.add(get_label(x=10.75 * cm, y=13.5 * cm, text='负责人：', size=10))
    d2.add(get_label(x=10.75 * cm, y=12.5 * cm, text='经办人：', size=10))
    d2.add(get_label(x=16.75 * cm, y=12.5 * cm, text='公章', size=10))
    d2.add(get_label(x=16.75 * cm, y=11.5 * cm, text='年\0\0\0月\0\0\0日', size=10))
    d2.add(get_label(x=3.25 * cm, y=10.25 * cm, text='区县（市）住房保障部门意见：', size=10))
    d2.add(get_label(x=1.45 * cm, y=8.75 * cm, text='负责人：', size=10))
    d2.add(get_label(x=1.45 * cm, y=7.75 * cm, text='经办人：', size=10))
    d2.add(get_label(x=16.75 * cm, y=7.75 * cm, text='公章', size=10))
    d2.add(get_label(x=16.75 * cm, y=6.5 * cm, text='年\0\0\0月\0\0\0日', size=10))
    d2.add(get_label(x=3.25 * cm, y=5 * cm, text='市保障性住房管理办公室意见：', size=10))
    d2.add(get_label(x=16.75 * cm, y=1 * cm, text='年\0\0\0月\0\0\0日', size=10))
    elements.append(Spacer(0, 1.75 * cm))
    elements.append(d2)
    report_name = report_path + apply_id + ".pdf"
    doc = SimpleDocTemplate(main_path + report_name,
                            topMargin=0.6 * cm,
                            leftMargin=0.7 * cm,
                            rightMargin=0.6 * cm,
                            bottomMargin=0 * cm, title=apply_id)
    doc.build(elements)
    return report_name


class ReportView(MethodView):
    """报表请求页面
    """
    def get(self):
        apply_id = request.args.get('apply_id', '')
        if apply_id == '':
            return render_template('applyreport.html', menu0='active open', menu0_3='active', pagename='申请审批表')
        else:
            report_name = get_apply_table(apply_id)
            return render_template('applyreport.html', menu0='active open', menu0_3='active', pagename='申请审批表',
                                   report_name=report_name)

    def post(self):
        pass
        # token = request.headers.get('token')
        # user = User('', '', token)
        # re = user.verify_token()
        # if re != 0:
        #     result = {'status': 'expired', 'info': '登录过期'}
        #     return jsonify(result)
        # apply_id = request.values.get('apply_id')
        # report_url = get_apply_table(apply_id)
        # print('the path is:' + report_url)
        # if report_url == 'not found':
        #     return jsonify({'status': 'fail', 'info': '没有查询到审批表信息！'})
        # else:
        #     return jsonify({'status': 'success', 'info': report_url})
