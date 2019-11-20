/**
 * 提交数据进行添加操作--房产出租信息
 */
function sendFormHouseRent(params) {
    var tx_house_code = document.getElementById("house_code");
    if (tx_house_code.value.trim() == null || tx_house_code.value.trim() == "") {
        alert('请输入产籍号！');
        tx_house_code.focus();
        return;
    }
    var tx_tenant_name = document.getElementById("tenant_name");
    if (tx_tenant_name.value.trim() == null || tx_tenant_name.value.trim() == "") {
        alert('请输入承租人信息！');
        tx_tenant_name.focus();
        return;
    }
    var tx_construction_area = document.getElementById("construction_area");
    if (tx_construction_area.value.trim() == null || tx_construction_area.value.trim() == "") {
        tx_construction_area.value = "0";
    }
    var tx_start_date = document.getElementById("start_date");
    if (tx_start_date.value.trim() == null || tx_start_date.value.trim() == "") {
        alert('请选择开始日期！');
        tx_start_date.focus();
        return;
    }
    var tx_end_date = document.getElementById("end_date");
    if (tx_end_date.value.trim() == null || tx_end_date.value.trim() == "") {
        alert('请选择结束日期！');
        tx_end_date.focus();
        return;
    }
    document.house_rent_form.submit();
}