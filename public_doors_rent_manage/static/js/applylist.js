
$(document).ready(function() {
    $("#menu-0-2").addClass("dropdown-toggle");
    $("#s-occur-date").val(get_now_formatdate());
    $("#e-occur-date").val(get_now_formatdate());
    if (verify_token() == "error") {
        window.location.href = "/login";
    }
});

/*
查询申请信息 按查询条件
*/
$.search_apply_list = function() {
    var s_date = $("#s-occur-date").val();
    var e_date = $("#e-occur-date").val();
    window.location.href = "/applylist?mode=search&s_date=" + s_date + "&e_date=" + e_date;
};

/*
查询申请信息
*/
$.search_apply_all = function() {
    window.location.href = "/applylist";
};

/*
跳转修改申请页面
*/
$.edit_apply_list = function(apply_id, state) {
    if (state == "未审批") {
        window.location.href = "apply?mode=edit&apply_id=" + apply_id;
    }
    else {
        alert("该申请信息已经被审批，无法修改");
    }
};

/*
跳转至申请信息详细页
*/
$.show_apply_list = function(apply_id) {
    window.location.href = 'apply?mode=show&apply_id=' + apply_id;
};

/*
删除申请信息操作
*/
$.del_apply_list = function(apply_id, state) {
    if (state != "未审批") {
        alert("该申请信息已经被审批，无法删除");
        return;
    }
    if(confirm("确定删除该申请信息吗？")) {
        $.ajax({
            url: "/applylist",
            type: "post",
            dataType: "json",
            headers: {
            "token": localStorage.getItem("token")
            },
            data: {"apply_id": apply_id},
            success: function(data) {
                if (String(data.status) == "success") {
                    alert("删除成功！");
                    window.location.href = '/applylist';
                }
                else if (String(data.status) == "approve") {
                    alert("该申请信息已经被审批，无法删除");
                }
                else if (String(data.status) == "expired") {
                    alert("登录已过期！");
                    window.location.href = '/login';
                }
                else {
                    alert("删除申请失败！" + String(data.info))
                }
            }
        });
    }
};