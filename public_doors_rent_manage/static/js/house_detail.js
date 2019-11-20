setHouseCodeInput();
/**
 * 提交数据进行添加操作--房产基本信息
 */
function sendFormHouseDetail(params) {
    var tx_house_code = document.getElementById("house_code");
    if (tx_house_code.value.trim() == null || tx_house_code.value.trim() == "") {
        alert('请输入产籍号！');
        tx_house_code.focus();
        return;
    }
    var tx_construction_area = document.getElementById("construction_area");
    if (tx_construction_area.value.trim() == null || tx_construction_area.value.trim() == "") {
        tx_construction_area.value = "0";
    }
    var tx_rent_area = document.getElementById("rent_area");
    if (tx_rent_area.value.trim() == null || tx_rent_area.value.trim() == "") {
        tx_rent_area.value = "0";
    }
    var tx_area_diff = document.getElementById("area_diff");
    if (tx_area_diff.value.trim() == null || tx_area_diff.value.trim() == "") {
        tx_area_diff.value = "0";
    }
    var tx_get_card_date = document.getElementById("get_card_date");
    if (tx_get_card_date.value.trim() == null || tx_get_card_date.value.trim() == "") {
        alert('请输入办证日期！');
        tx_get_card_date.focus();
        return;
    }
    document.house_detail_form.submit();
}
/**
 * 跳转到房产列表信息页
 */
function backToHouses() {
    //alert("hello");
    window.location.href='houses?mode=all';
}
/**
 * 根据传入的mode值，设定产籍号input的只读属性
 */
function setHouseCodeInput() {
    var li_mode = document.getElementById("li_mode");
    var house_code = document.getElementById("house_code");
    if (li_mode.innerText == "修改") {
        house_code.readOnly = true;
        //alert("fds");
    }
}
/**
 *
 */