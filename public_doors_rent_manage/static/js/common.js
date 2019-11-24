/*
验证token是否过期，如果没有过期，返回的data中带过来用户名
*/
function verify_token() {
    var re = '';
    $.ajax({
        url: "/token",
        type: "post",
        dataType: "json",
        headers: {"token": localStorage.getItem("token")},
        data: {"username": "123"},
        async: false,
        success: function(data){
            re = data.username;
            if (String(data.status) == "refresh_token") {
                localStorage.setItem("token", data.token);
            }
        }
    });
    console.log(re);
    return re;
}
/*
获得当前日期并格式化
*/
function get_now_formatdate() {
    var date = new Date();
    var seperator1 = "-";
    var year = date.getFullYear();
    var month = date.getMonth() + 1;
    var strDate = date.getDate();
    if (month >= 1 && month <= 9) {
        month = "0" + month;
    }
    if (strDate >= 0 && strDate <= 9) {
        strDate = "0" + strDate;
    }
    var currentdate = year + seperator1 + month + seperator1 + strDate;
    return currentdate;
};
/*
查询申请审批表
*/
$.search_apply_table = function(apply_id, mode) {
    if (apply_id == "") {
        return;
    }
    window.location.href = "/approve?mode=" + mode + "&apply_id=" + apply_id
};
/*
修改密码
*/
$.change_password = function(old_pw, new_pw1, new_pw2) {
    if (old_pw == "") {
        alert("请输入原密码！");
        return;
    }
    if (new_pw1 == "" || new_pw2 == "") {
        alert("请输入新密码！");
        return;
    }
    if (new_pw1 != new_pw2) {
        alert("两次新密码输入不一致！");
        return;
    }
    $.ajax({
        url: "/common",
        type: "post",
        dataType: "json",
        headers: {
        "opt_type": "change_password",
        "token": localStorage.getItem("token")
        },
        data: {
        "old_pw": old_pw,
        "new_pw": new_pw1
        },
        success: function(data) {
            if (String(data.status) == "success") {
                alert("修改完成！");
            }
            else if (String(data.status) == "expired") {
                alert(String(data.info));
                window.location.href = "/login";
            }
            else if (String(data.status) == "error") {
                alert(String(data.info));
            }
            else {
                alert("修改密码失败！" + String(data.info));
            }
        }
    });
};
/*
注销
*/
$.logout = function() {
    localStorage.removeItem("token");
    window.location.href = "/login";
}