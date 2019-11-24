$(document).ready(function() {
    $("#menu-0-3").addClass("dropdown-toggle");
    $("#s-occur-date").val(get_now_formatdate());
    $("#e-occur-date").val(get_now_formatdate());
    if (verify_token() == "error") {
        window.location.href = "/login";
    }
});
/*
查询申请信息
*/
$.search_applylist_all = function() {
    window.location.href = "/reports?mode=applyreport";
};
/*
按查询条件查询申请明细表
*/
$.search_applylist_report = function() {
    var s_date = $("#s-occur-date").val();
    var e_date = $("#e-occur-date").val();
    var state = $("#state-str").val();
    window.location.href = "/reports?mode=applyreport_search&s_date=" + s_date + "&e_date=" + e_date + "&state=" + state;
};