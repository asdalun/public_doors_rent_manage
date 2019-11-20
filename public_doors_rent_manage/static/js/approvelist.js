$(document).ready(function() {
    $("#s-approve-date").val(get_now_formatdate())
    $("#e-approve-date").val(get_now_formatdate())
    if (verify_token() == "error") {
        window.location.href = "/login";
    }
});
/*
查询申请信息
*/
$.search_approve_all = function() {
    window.location.href = "/approvelist?mode=" + $("#mode").val();
}
/*
查询街道审批信息 按查询条件
*/
$.search_apply_list = function() {
    var s_date = $("#s-approve-date").val();
    var e_date = $("#e-approve-date").val();
    window.location.href = "/approvelist?mode=" + $("#mode").val() + "search&s_date=" + s_date + "&e_date=" + e_date;
}