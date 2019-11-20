
function onlyNum(that){
    that.value=that.value.replace(/\D/g,"");
}

$(document).ready(function () {
    $("#menu-0-1").addClass("dropdown-toggle");
    var mode = $("#mode").val();
    if (mode == "add" || mode == "") {
        $("#man").attr("checked", "true");
        $("#married").attr("checked", "true");
        $("#occur-date").val(get_now_formatdate())
        $("#street-name").empty();
        $("#community-name").empty();
        $.get_street_and_community();
    }
    else if (mode == "edit" || mode == "show") {
        $("#apply-id").attr("readonly", "true");
        if ($("#sex").val() != "女") {
            $("#man").attr("checked", "true");
        }
        else {
            $("#woman").attr("checked", "true");
        }
        if ($("#marital-status").val() != "单身") {
            $("#married").attr("checked", "true");
        }
        else {
            $("#unmarried").attr("checked", "true");
        }
        if ($("#unit-pro-bussiness").val() == "1") {
            $("#cb-unit-pro-bussiness").attr("checked", "true");
        }
        if ($("#unit-pro-office").val() == "1") {
            $("#cb-unit-pro-office").attr("checked", "true");
        }
        if ($("#unit-pro-employment").val() == "1") {
            $("#cb-unit-pro-employment").attr("checked", "true");
        }
        if ($("#unit-pro-retire").val() == "1") {
            $("#cb-unit-pro-retire").attr("checked", "true");
        }
        if ($("#unit-pro-other").val() == "1") {
            $("#cb-unit-pro-other").attr("checked", "true");
        }
        if ($("#pro-graduate").val() == "1") {
            $("#cb-pro-graduate").attr("checked", "true");
        }
        if ($("#pro-outside").val() == "1") {
            $("#cb-pro-outside").attr("checked", "true");
        }
        if ($("#pro-gov-talent").val() == "1") {
            $("#cb-pro-gov-talent").attr("checked", "true");
        }
        if ($("#pro-difficult").val() == "1") {
            $("#cb-pro-difficult").attr("checked", "true");
        }
        if ($("#pro-cheap").val() == "1") {
            $("#cb-pro-cheap").attr("checked", "true");
        }
        if ($("#pro-economy").val() == "1") {
            $("#cb-pro-economy").attr("checked", "true");
        }
        if ($("#is-transfer").val() == "1") {
            $("#cb-is-transfer").attr("checked", "true");
        }
        if ($("#is-remove").val() == "1") {
            $("#cb-is-remove").attr("checked", "true");
        }
        $.get_street_and_community();
    }
    if (mode == "show") {
        $("#apply-id").attr("readonly", "true");
        $("#btn-save").hide();
        $("#btn-reset").hide();
    }
    if (verify_token() == "error") {
        window.location.href = "/login";
    }
});

/*
查询登录用户所属的街道和社区
*/
$.get_street_and_community = function() {
    $.ajax({
        url: "/common",
        type: "get",
        dataType: "json",
        headers: {
        "opt_type": "get_street_and_community",
        "token": localStorage.getItem("token")
        },
        data: {},
        success: function(data) {
            if (String(data.status) == "success") {
                $.each(data.streets, function(i, item){
                    var $option = $("<option value='" + item.street_name + "'>" + item.street_name + "</option>");
                    $("#street-name").append($option);
                }) 
                $.each(data.communities, function(i, item){
                    var $option = $("<option value='" + item.community_name + "'>" + item.community_name + "</option>");
                    $("#community-name").append($option);
                }) 
            }
            else {
                alert("获取街道和社区信息失败！" + String(data.info))
            }
        }
    });
};

/*
计算合计年收入
*/
$.get_all_income = function() {
    if ($("#member-income-1").val() == '') {
        $("#member-income-1").val('0');
    }
    if ($("#member-income-2").val() == '') {
        $("#member-income-2").val('0');
    }
    if ($("#member-income-3").val() == '') {
        $("#member-income-3").val('0');
    }
    if ($("#member-income-4").val() == '') {
        $("#member-income-4").val('0');
    }
    if ($("#member-income-5").val() == '') {
        $("#member-income-5").val('0');
    }
    var _all_income = parseFloat($("#member-income-1").val()) + parseFloat($("#member-income-2").val()) +
                    parseFloat($("#member-income-3").val()) + parseFloat($("#member-income-4").val()) +
                    parseFloat($("#member-income-5").val());
    $("#all-come").val(_all_income);
    return _all_income;
};

/*
新增申请信息
*/
$.add_apply = function() {
    //参数字典
    var _params = new Array();
    var _apply_id = $("#apply-id").val();
    if(_apply_id == "") {
        alert("请输入申请编号！");
        $("#apply-id").focus();
        return;
    }
    _params["_apply_id"] = _apply_id;
    var _tenant_name = $("#tenant-name").val();
    if (_tenant_name == "") {
        alert("请输入申请人姓名！");
        $("#tenant-name").focus();
        return;
    }
    _params["_tenant_name"] = _tenant_name;
    var _tenant_IDcode = $("#tenant-IDcode").val();
    if (_tenant_IDcode == "") {
        alert("请输入申请人身份证号码！");
        $("#tenant-IDcode").focus();
        return;
    }
    _params["_tenant_IDcode"] = _tenant_IDcode;
    _params["_sex"] = $("input[name='sex-radio']:checked").val();
    _params["_marital_status"] = $("input[name='marray-radio']:checked").val();
    _params["_tenant_unit"] = $("#tenant-unit").val();
    _params["_tenant_unit_address"] = $("#tenant-unit-address").val();
    var _unit_pro_business = 0;
    if ($('#cb-unit-pro-business').is(':checked')) {
        _unit_pro_business = "1";
    }
    _params["_unit_pro_business"] = _unit_pro_business;
    var _unit_pro_office = "0";
    if ($('#cb-unit-pro-office').is(':checked')) {
        _unit_pro_office = "1";
    }
    _params["_unit_pro_office"] = _unit_pro_office;
    var _unit_pro_employment = 0;
    if ($('#cb-unit-pro-employment').is(':checked')) {
        _unit_pro_employment = 1;
    }
    _params["_unit_pro_employment"] = _unit_pro_employment;
    var _unit_pro_retire = 0;
    if ($('#cb-unit-pro-retire').is(':checked')) {
        _unit_pro_retire = 1;
    }
    _params["_unit_pro_retire"] = _unit_pro_retire;
    var _unit_pro_other = 0;
    if ($('#cb-unit-pro-other').is(':checked')) {
        _unit_pro_other = 1;
    }
    _params["_unit_pro_other"] = _unit_pro_other;
    _params["_card_address"] = $("#card-address").val();
    _params["_now_address"] = $("#now-address").val();
    var _pro_graduate = 0;
    if ($('#cb-pro-graduate').is(':checked')) {
        _pro_graduate = 1;
    }
    _params["_pro_graduate"] = _pro_graduate;
    var _pro_outside = 0;
    if ($('#cb-pro-outside').is(':checked')) {
        _pro_outside = 1;
    }
    _params["_pro_outside"] = _pro_outside;
    var _pro_gov_talent = 0;
    if ($('#cb-pro-gov-talent').is(':checked')) {
        _pro_gov_talent = 1;
    }
    _params["_pro_gov_talent"] = _pro_gov_talent;
    var _pro_difficult = 0;
    if ($('#cb-pro-difficult').is(':checked')) {
        _pro_difficult = 1;
    }
    _params["_pro_difficult"] = _pro_difficult;
    var _pro_cheap = 0;
    if ($('#cb-pro-cheap').is(':checked')) {
        _pro_cheap = 1;
    }
    _params["_pro_cheap"] = _pro_cheap;
    var _pro_economy = 0;
    if ($('#cb-pro-economy').is(':checked')) {
        _pro_economy = 1;
    }
    _params["_pro_economy"] = _pro_economy;
    _params["_minimum_living_no"] = $("#minimum-living-no").val();
    _params["_occur_date"] = $("#occur-date").val();
    _params["_remark"] = $("#remark").val();
    $("#income-all").val($.get_all_income())
    _params["_all_income"] = $("#income-all").val();
    _params["_member_name_1"] = $("#member-name-1").val();
    _params["_member_relation_1"] = $("#member-relation-1").val();
    _params["_member_ID_1"] = $("#member-ID-1").val();
    _params["_member_unit_1"] = $("#member-unit-1").val();
    if ($("#member-income-1").val() == '') {
        $("#member-income-1").val('0');
    }
    _params["_member_income_1"] = $("#member-income-1").val();
    _params["_member_name_2"] = $("#member-name-2").val();
    _params["_member_relation_2"] = $("#member-relation-2").val();
    _params["_member_ID_2"] = $("#member-ID-2").val();
    _params["_member_unit_2"] = $("#member-unit-2").val();
    if ($("#member-income-2").val() == '') {
        $("#member-income-2").val('0');
    }
    _params["_member_income_2"] = $("#member-income-2").val();
    _params["_member_name_3"] = $("#member-name-3").val();
    _params["_member_relation_3"] = $("#member-relation-3").val();
    _params["_member_ID_3"] = $("#member-ID-3").val();
    _params["_member_unit_3"] = $("#member-unit-3").val();
    if ($("#member-income-3").val() == '') {
        $("#member-income-3").val('0');
    }
    _params["_member_income_3"] = $("#member-income-3").val();
    _params["_member_name_4"] = $("#member-name-4").val();
    _params["_member_relation_4"] = $("#member-relation-4").val();
    _params["_member_ID_4"] = $("#member-ID-4").val();
    _params["_member_unit_4"] = $("#member-unit-4").val();
    if ($("#member-income-4").val() == '') {
        $("#member-income-4").val('0');
    }
    _params["_member_income_4"] = $("#member-income-4").val();
    _params["_member_name_5"] = $("#member-name-5").val();
    _params["_member_relation_5"] = $("#member-relation-5").val();
    _params["_member_ID_5"] = $("#member-ID-5").val();
    _params["_member_unit_5"] = $("#member-unit-5").val();
    if ($("#member-income-5").val() == '') {
        $("#member-income-5").val('0');
    }
    _params["_member_income_5"] = $("#member-income-5").val();
    if ($("#income-avg").val() == '') {
        $("#income-avg").val('0');
    }
    _params["_income_avg"] = $("#income-avg").val();
    _params["_member_name_11"] = $("#member-name-11").val();
    _params["_member_address_11"] = $("#member-address-11").val();
    if ($("#member-con-area-11").val() == '') {
        $("#member-con-area-11").val('0');
    }
    _params["_member_con_area_11"] = $("#member-con-area-11").val();
    _params["_member_door_prop_11"] = $("#member-door-prop-11").val();
    _params["_member_name_12"] = $("#member-name-12").val();
    _params["_member_address_12"] = $("#member-address-12").val();
    if ($("#member-con-area-12").val() == '') {
        $("#member-con-area-12").val('0');
    }
    _params["_member_con_area_12"] = $("#member-con-area-12").val();
    _params["_member_door_prop_12"] = $("#member-door-prop-12").val();
    var _is_transfer = 0;
    if ($('#cb-is-transfer').is(':checked')) {
        _is_transfer = 1;
    }
    _params["_is_transfer"] = _is_transfer;
    _params["_transfer_addres_1"] = $("#transfer-address-1").val();
    if ($("#transfer-con-area-1").val() == "")
        $("#transfer-con-area-1").val("0");
    _params["_transfer_con_area_1"] = parseFloat($("#transfer-con-area-1").val());
    var _is_remove = 0;
    if ($('#cb-is-remove').is(':checked')) {
        _is_remove = 1;
    }
    _params["_is_remove"] = _is_remove;
    _params["_remove_addres_1"] = $("#remove-address-1").val();
    if ($("#remove-con-area-1").val() == "")
        $("#remove-con-area-1").val("0");
    _params["_remove_con_area_1"] = parseFloat($("#remove-con-area-1").val());
    if ($("#con-area-avg").val() == "")
        $("#con-area-avg").val("0");
    _params["_con_area_avg"] = parseFloat($("#con-area-avg").val());
    _params["_street_name"] = $("#street-name").val();
    _params["_community_name"] = $("#community-name").val();
    _params["_transfer_pro_1"] = $("#transfer-pro-1").val();
    _params["_remove_pro_1"] = $("#remvoe-pro-1").val();
    $.ajax({
        url: "/apply",
        type: "post",
        dataType: "json",
        headers: {"sub_type": "add", "token": localStorage.getItem("token")},
        data: {
        "_apply_id": _params["_apply_id"],
        "_tenant_name": _params["_tenant_name"],
        "_tenant_IDcode": _params["_tenant_IDcode"],
        "_sex": _params["_sex"],
        "_marital_status": _params["_marital_status"],
        "_tenant_unit": _params["_tenant_unit"],
        "_tenant_unit_address": _params["_tenant_unit_address"],
        "_unit_pro_business": _params["_unit_pro_business"],
        "_unit_pro_office": _params["_unit_pro_office"],
        "_unit_pro_employment": _params["_unit_pro_employment"],
        "_unit_pro_retire": _params["_unit_pro_retire"],
        "_unit_pro_other": _params["_unit_pro_other"],
        "_card_address": _params["_card_address"],
        "_now_address": _params["_now_address"],
        "_pro_graduate": _params["_pro_graduate"],
        "_pro_outside": _params["_pro_outside"],
        "_pro_gov_talent": _params["_pro_gov_talent"],
        "_pro_difficult": _params["_pro_difficult"],
        "_pro_cheap": _params["_pro_cheap"],
        "_pro_economy": _params["_pro_economy"],
        "_minimum_living_no": _params["_minimum_living_no"],
        "_occur_date": _params["_occur_date"],
        "_remark": _params["_remark"],
        "_all_income": _params["_all_income"],
        "_member_name_1": _params["_member_name_1"],
        "_member_relation_1": _params["_member_relation_1"],
        "_member_ID_1": _params["_member_ID_1"],
        "_member_unit_1": _params["_member_unit_1"],
        "_member_income_1": _params["_member_income_1"],
        "_member_name_2": _params["_member_name_2"],
        "_member_relation_2": _params["_member_relation_2"],
        "_member_ID_2": _params["_member_ID_2"],
        "_member_unit_2": _params["_member_unit_2"],
        "_member_income_2": _params["_member_income_2"],
        "_member_name_3": _params["_member_name_3"],
        "_member_relation_3": _params["_member_relation_3"],
        "_member_ID_3": _params["_member_ID_3"],
        "_member_unit_3": _params["_member_unit_3"],
        "_member_income_3": _params["_member_income_3"],
        "_member_name_4": _params["_member_name_4"],
        "_member_relation_4": _params["_member_relation_4"],
        "_member_ID_4": _params["_member_ID_4"],
        "_member_unit_4": _params["_member_unit_4"],
        "_member_income_4": _params["_member_income_4"],
        "_member_name_5": _params["_member_name_5"],
        "_member_relation_5": _params["_member_relation_5"],
        "_member_ID_5": _params["_member_ID_5"],
        "_member_unit_5": _params["_member_unit_5"],
        "_member_income_5": _params["_member_income_5"],
        "_income_avg": _params["_income_avg"],
        "_member_name_11": _params["_member_name_11"],
        "_member_address_11": _params["_member_address_11"],
        "_member_con_area_11": _params["_member_con_area_11"],
        "_member_door_prop_11": _params["_member_door_prop_11"],
        "_member_name_12": _params["_member_name_12"],
        "_member_address_12": _params["_member_address_12"],
        "_member_con_area_12": _params["_member_con_area_12"],
        "_member_door_prop_12": _params["_member_door_prop_12"],
        "_is_transfer": _params["_is_transfer"],
        "_transfer_addres_1": _params["_transfer_addres_1"],
        "_transfer_con_area_1": _params["_transfer_con_area_1"],
        "_is_remove": _params["_is_remove"],
        "_remove_addres_1": _params["_remove_addres_1"],
        "_remove_con_area_1": _params["_remove_con_area_1"],
        "_con_area_avg": _params["_con_area_avg"],
        "_street_name": _params["_street_name"],
        "_community_name": _params["_community_name"],
        "_transfer_pro_1": _params["_transfer_pro_1"],
        "_remove_pro_1": _params["_remove_pro_1"]
        },
        success: function(data){
            if (String(data.status) == "success") {
                alert("保存成功！");
            }
            else if (String(data.status) == "expired") {
                alert("登录已过期！");
                window.location.href = "/login";
            }
            else if (String(data.status) == "repeat") {
                alert("申请编号重复!");
                $("#apply-id").focus();
            }
            else if (String(data.status) == "fail") {
                alert("保存数据失败！" + String(data.info))
            }
        }
    });
}

/*
修改申请信息
*/
$.edit_apply = function() {
    //参数字典
    var _params = new Array();
    _params["_apply_id"] = $("#apply-id").val();
    var _tenant_name = $("#tenant-name").val();
    if (_tenant_name == "") {
        alert("请输入申请人姓名！");
        $("#tenant-name").focus();
        return;
    }
    _params["_tenant_name"] = _tenant_name;
    var _tenant_IDcode = $("#tenant-IDcode").val();
    if (_tenant_IDcode == "") {
        alert("请输入申请人身份证号码！");
        $("#tenant-IDcode").focus();
        return;
    }
    _params["_tenant_IDcode"] = _tenant_IDcode;
    _params["_sex"] = $("input[name='sex-radio']:checked").val();
    _params["_marital_status"] = $("input[name='marray-radio']:checked").val();
    _params["_tenant_unit"] = $("#tenant-unit").val();
    _params["_tenant_unit_address"] = $("#tenant-unit-address").val();
    var _unit_pro_business = 0;
    if ($('#cb-unit-pro-business').is(':checked')) {
        _unit_pro_business = "1";
    }
    _params["_unit_pro_business"] = _unit_pro_business;
    var _unit_pro_office = "0";
    if ($('#cb-unit-pro-office').is(':checked')) {
        _unit_pro_office = "1";
    }
    _params["_unit_pro_office"] = _unit_pro_office;
    var _unit_pro_employment = 0;
    if ($('#cb-unit-pro-employment').is(':checked')) {
        _unit_pro_employment = 1;
    }
    _params["_unit_pro_employment"] = _unit_pro_employment;
    var _unit_pro_retire = 0;
    if ($('#cb-unit-pro-retire').is(':checked')) {
        _unit_pro_retire = 1;
    }
    _params["_unit_pro_retire"] = _unit_pro_retire;
    var _unit_pro_other = 0;
    if ($('#cb-unit-pro-other').is(':checked')) {
        _unit_pro_other = 1;
    }
    _params["_unit_pro_other"] = _unit_pro_other;
    _params["_card_address"] = $("#card-address").val();
    _params["_now_address"] = $("#now-address").val();
    var _pro_graduate = 0;
    if ($('#cb-pro-graduate').is(':checked')) {
        _pro_graduate = 1;
    }
    _params["_pro_graduate"] = _pro_graduate;
    var _pro_outside = 0;
    if ($('#cb-pro-outside').is(':checked')) {
        _pro_outside = 1;
    }
    _params["_pro_outside"] = _pro_outside;
    var _pro_gov_talent = 0;
    if ($('#cb-pro-gov-talent').is(':checked')) {
        _pro_gov_talent = 1;
    }
    _params["_pro_gov_talent"] = _pro_gov_talent;
    var _pro_difficult = 0;
    if ($('#cb-pro-difficult').is(':checked')) {
        _pro_difficult = 1;
    }
    _params["_pro_difficult"] = _pro_difficult;
    var _pro_cheap = 0;
    if ($('#cb-pro-cheap').is(':checked')) {
        _pro_cheap = 1;
    }
    _params["_pro_cheap"] = _pro_cheap;
    var _pro_economy = 0;
    if ($('#cb-pro-economy').is(':checked')) {
        _pro_economy = 1;
    }
    _params["_pro_economy"] = _pro_economy;
    _params["_minimum_living_no"] = $("#minimum-living-no").val();
    _params["_occur_date"] = $("#occur-date").val();
    _params["_remark"] = $("#remark").val();
    $("#income-all").val($.get_all_income())
    _params["_all_income"] = $("#income-all").val();
    _params["_member_name_1"] = $("#member-name-1").val();
    _params["_member_relation_1"] = $("#member-relation-1").val();
    _params["_member_ID_1"] = $("#member-ID-1").val();
    _params["_member_unit_1"] = $("#member-unit-1").val();
    if ($("#member-income-1").val() == '') {
        $("#member-income-1").val('0');
    }
    _params["_member_income_1"] = $("#member-income-1").val();
    _params["_member_name_2"] = $("#member-name-2").val();
    _params["_member_relation_2"] = $("#member-relation-2").val();
    _params["_member_ID_2"] = $("#member-ID-2").val();
    _params["_member_unit_2"] = $("#member-unit-2").val();
    if ($("#member-income-2").val() == '') {
        $("#member-income-2").val('0');
    }
    _params["_member_income_2"] = $("#member-income-2").val();
    _params["_member_name_3"] = $("#member-name-3").val();
    _params["_member_relation_3"] = $("#member-relation-3").val();
    _params["_member_ID_3"] = $("#member-ID-3").val();
    _params["_member_unit_3"] = $("#member-unit-3").val();
    if ($("#member-income-3").val() == '') {
        $("#member-income-3").val('0');
    }
    _params["_member_income_3"] = $("#member-income-3").val();
    _params["_member_name_4"] = $("#member-name-4").val();
    _params["_member_relation_4"] = $("#member-relation-4").val();
    _params["_member_ID_4"] = $("#member-ID-4").val();
    _params["_member_unit_4"] = $("#member-unit-4").val();
    if ($("#member-income-4").val() == '') {
        $("#member-income-4").val('0');
    }
    _params["_member_income_4"] = $("#member-income-4").val();
    _params["_member_name_5"] = $("#member-name-5").val();
    _params["_member_relation_5"] = $("#member-relation-5").val();
    _params["_member_ID_5"] = $("#member-ID-5").val();
    _params["_member_unit_5"] = $("#member-unit-5").val();
    if ($("#member-income-5").val() == '') {
        $("#member-income-5").val('0');
    }
    _params["_member_income_5"] = $("#member-income-5").val();
    if ($("#income-avg").val() == '') {
        $("#income-avg").val('0');
    }
    _params["_income_avg"] = $("#income-avg").val();
    _params["_member_name_11"] = $("#member-name-11").val();
    _params["_member_address_11"] = $("#member-address-11").val();
    if ($("#member-con-area-11").val() == '') {
        $("#member-con-area-11").val('0');
    }
    _params["_member_con_area_11"] = $("#member-con-area-11").val();
    _params["_member_door_prop_11"] = $("#member-door-prop-11").val();
    _params["_member_name_12"] = $("#member-name-12").val();
    _params["_member_address_12"] = $("#member-address-12").val();
    if ($("#member-con-area-12").val() == '') {
        $("#member-con-area-12").val('0');
    }
    _params["_member_con_area_12"] = $("#member-con-area-12").val();
    _params["_member_door_prop_12"] = $("#member-door-prop-12").val();
    var _is_transfer = 0;
    if ($('#cb-is-transfer').is(':checked')) {
        _is_transfer = 1;
    }
    _params["_is_transfer"] = _is_transfer;
    _params["_transfer_addres_1"] = $("#transfer-address-1").val();
    if ($("#transfer-con-area-1").val() == "")
        $("#transfer-con-area-1").val("0");
    _params["_transfer_con_area_1"] = parseFloat($("#transfer-con-area-1").val());
    var _is_remove = 0;
    if ($('#cb-is-remove').is(':checked')) {
        _is_remove = 1;
    }
    _params["_is_remove"] = _is_remove;
    _params["_remove_addres_1"] = $("#remove-address-1").val();
    if ($("#remove-con-area-1").val() == "")
        $("#remove-con-area-1").val("0");
    _params["_remove_con_area_1"] = parseFloat($("#remove-con-area-1").val());
    if ($("#con-area-avg").val() == "")
        $("#con-area-avg").val("0");
    _params["_con_area_avg"] = parseFloat($("#con-area-avg").val());
    _params["_street_name"] = $("#street-name").val();
    _params["_community_name"] = $("#community-name").val();
    _params["_transfer_pro_1"] = $("#transfer-pro-1").val();
    _params["_remove_pro_1"] = $("#remove-pro-1").val();
    $.ajax({
        url: "/apply",
        type: "post",
        dataType: "json",
        headers: {"sub_type": "edit", "token": localStorage.getItem("token")},
        data: {
        "_apply_id": _params["_apply_id"],
        "_tenant_name": _params["_tenant_name"],
        "_tenant_IDcode": _params["_tenant_IDcode"],
        "_sex": _params["_sex"],
        "_marital_status": _params["_marital_status"],
        "_tenant_unit": _params["_tenant_unit"],
        "_tenant_unit_address": _params["_tenant_unit_address"],
        "_unit_pro_business": _params["_unit_pro_business"],
        "_unit_pro_office": _params["_unit_pro_office"],
        "_unit_pro_employment": _params["_unit_pro_employment"],
        "_unit_pro_retire": _params["_unit_pro_retire"],
        "_unit_pro_other": _params["_unit_pro_other"],
        "_card_address": _params["_card_address"],
        "_now_address": _params["_now_address"],
        "_pro_graduate": _params["_pro_graduate"],
        "_pro_outside": _params["_pro_outside"],
        "_pro_gov_talent": _params["_pro_gov_talent"],
        "_pro_difficult": _params["_pro_difficult"],
        "_pro_cheap": _params["_pro_cheap"],
        "_pro_economy": _params["_pro_economy"],
        "_minimum_living_no": _params["_minimum_living_no"],
        "_occur_date": _params["_occur_date"],
        "_remark": _params["_remark"],
        "_all_income": _params["_all_income"],
        "_member_name_1": _params["_member_name_1"],
        "_member_relation_1": _params["_member_relation_1"],
        "_member_ID_1": _params["_member_ID_1"],
        "_member_unit_1": _params["_member_unit_1"],
        "_member_income_1": _params["_member_income_1"],
        "_member_name_2": _params["_member_name_2"],
        "_member_relation_2": _params["_member_relation_2"],
        "_member_ID_2": _params["_member_ID_2"],
        "_member_unit_2": _params["_member_unit_2"],
        "_member_income_2": _params["_member_income_2"],
        "_member_name_3": _params["_member_name_3"],
        "_member_relation_3": _params["_member_relation_3"],
        "_member_ID_3": _params["_member_ID_3"],
        "_member_unit_3": _params["_member_unit_3"],
        "_member_income_3": _params["_member_income_3"],
        "_member_name_4": _params["_member_name_4"],
        "_member_relation_4": _params["_member_relation_4"],
        "_member_ID_4": _params["_member_ID_4"],
        "_member_unit_4": _params["_member_unit_4"],
        "_member_income_4": _params["_member_income_4"],
        "_member_name_5": _params["_member_name_5"],
        "_member_relation_5": _params["_member_relation_5"],
        "_member_ID_5": _params["_member_ID_5"],
        "_member_unit_5": _params["_member_unit_5"],
        "_member_income_5": _params["_member_income_5"],
        "_income_avg": _params["_income_avg"],
        "_member_name_11": _params["_member_name_11"],
        "_member_address_11": _params["_member_address_11"],
        "_member_con_area_11": _params["_member_con_area_11"],
        "_member_door_prop_11": _params["_member_door_prop_11"],
        "_member_name_12": _params["_member_name_12"],
        "_member_address_12": _params["_member_address_12"],
        "_member_con_area_12": _params["_member_con_area_12"],
        "_member_door_prop_12": _params["_member_door_prop_12"],
        "_is_transfer": _params["_is_transfer"],
        "_transfer_addres_1": _params["_transfer_addres_1"],
        "_transfer_con_area_1": _params["_transfer_con_area_1"],
        "_is_remove": _params["_is_remove"],
        "_remove_addres_1": _params["_remove_addres_1"],
        "_remove_con_area_1": _params["_remove_con_area_1"],
        "_con_area_avg": _params["_con_area_avg"],
        "_street_name": _params["_street_name"],
        "_community_name": _params["_community_name"],
        "_transfer_pro_1": _params["_transfer_pro_1"],
        "_remove_pro_1": _params["_remove_pro_1"]
        },
        success: function(data){
            if (String(data.status) == "success") {
                alert("保存成功！");
            }
            else if (String(data.status) == "expired") {
                alert("登录已过期！");
                window.location.href = "/login";
            }
            else if (String(data.status) == "fail") {
                alert("保存数据失败！" + String(data.info))
            }
        }
    });
}

$(function() {
    /*
    当选择街道时，获取对应的社区信息
    */
    $("#street-name").change(function() {
        $("#community-name").empty();
        var $option = $("<option value=''></option>");
        $("#community-name").append($option);
        street_name = $("#street-name").val()
        $.ajax({
            url: "/common",
            type: "get",
            dataType: "json",
            headers: {"opt_type": "get_community_name"},
            data:{"street_name": street_name},
            success: function(data){
                if (String(data.status) == "success") {
                    $.each(data.communities, function(i, item){
                        var $option = $("<option value='" + item.community_name + "'>" + item.community_name + "</option>");
                        $("#community-name").append($option);
                    }) 
                }
                else {
                    alert("获取街道和社区信息失败！" + String(data.info))
                }
            }
        });
    });

    /*
    收入合计得到焦点后计算
    */
    $("#income-all").focus(function() {
        var _all_income = $.get_all_income();
        $("#income-all").val(_all_income);
    });

    /*
    保存申请信息
    */
    $("#btn-save").click(function() {
        var mode = $("#mode").val();
        if (mode == "add" || mode == "") {
            $.add_apply();
        }
        else {
            $.edit_apply();
        }
    });

    /*
    重置申请信息
    */
    $("#btn-reset").click(function() {
        var mode = $("#mode").val();
        if (mode == "add") {
            $("#apply-id").val("");
            $("#tenant-name").val("");
            $("#tenant-IDcode").val("");
            $("#occur-date").val(get_now_formatdate())
            $("#tenant-unit").val("");
            $("#tenant-unit-address").val("");
            $('input:checkbox').attr("checked", false);
            $("#card-address").val("");
            $("#now-address").val("");
            $("#minimum-living-no").val("");
            $("#remark").val("");
            $("#member-name-1").val("");
            $("#member-relation-1").val("");
            $("#member-ID-1").val("");
            $("#member-unit-1").val("");
            $("#member-income-1").val('0');
            $("#member-name-2").val("");
            $("#member-relation-2").val("");
            $("#member-ID-2").val("");
            $("#member-unit-2").val("");
            $("#member-income-2").val('0');
            $("#member-name-3").val("");
            $("#member-relation-3").val("");
            $("#member-ID-3").val("");
            $("#member-unit-3").val("");
            $("#member-income-3").val('0');
            $("#member-name-4").val("");
            $("#member-relation-4").val("");
            $("#member-ID-4").val("");
            $("#member-unit-4").val("");
            $("#member-income-4").val('0');
            $("#member-name-5").val("");
            $("#member-relation-5").val("");
            $("#member-ID-5").val("");
            $("#member-unit-5").val("");
            $("#member-income-5").val("0");
            $("#income-avg").val("0");
            $("#all-come").val("0");
            $("#member-name-11").val("");
            $("#member-address-11").val("");
            $("#member-con-area-11").val("0");
            $("#member-door-prop-11").val("");
            $("#member-name-12").val("");
            $("#member-address-12").val("");
            $("#member-con-area-12").val("0");
            $("#member-door-prop-12").val("");
            $("#transfer-address-1").val("");
            $("#transfer_con_area_1").val("0");
            $("#remove-address-1").val("");
            $("#remove_con_area_1").val("0");
            $("#con-area-avg").val("0");
        }
    })
});
