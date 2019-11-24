///**
// * 提交登录表单
// */
//function sendForm() {
//    if (checkForm()) {
//        //alert("hello1");
//        var loginForm = document.getElementsByName('loginForm')
//        loginForm.submit();
//        return true;
//    }
//    else {
//        //alert("hello2");
//        return false;
//    }
//
//}
///**
// * 检查表单输入判断
// */
//function checkForm() {
//    var input_username = document.getElementById('username');
//    var input_password = document.getElementById('password');
//    var p_logintext = document.getElementById('logintext');
//    if (input_username.value == "" || input_password.value == "") {
//
//        p_logintext.innerHTML = "*请输入用户名和密码";
//        return false;
//    }
//    else {
//        p_logintext.innerHTML = "";
//        return true;
//    }
//}
///**
// * 重置表单
// */
//function resetForm() {
//    var input_username = document.getElementById('username');
//    var input_password = document.getElementById('password');
//    input_username.value = "";
//    input_password.value = "";
//    input_username.focus();
//}
//
//
//$("loginBtn").click(function()) {
//    alert("hahahah");
//    $.post("login.json",
//        //发送给后端的数据
//        {
//            "name":$("#username").val(),
//            "password":$("#password").val()
//        },
//        //回调函数
//        function(data){
//            var json=data[0];
//            if(json.success == 0){
//                $("#errormessage").text("用户名或密码错误");
//            }
//            else if(json.success== 1){
//                window.location.href="index.html";
//            }
//        }
//    )
//}



$(function(){
    //进行token验证，成功后，跳转到对应的url
    $.jump_to_token = function(_username, url) {
        $.ajax({
            url: "/token",
            type: "get",
            dataType: "json",
            headers: {"token": localStorage.getItem("token")},
            data: {username: _username},
            success: function(data){
                if (String(data.status) == "ok") {
                    window.location.href = url + "?username=" + data.username;
                }
                else if (String(data.status) == "refresh_token") {
                    localStorage.setItem("token", data.token);
                    window.location.href = url + "?username=" + data.username;
                }
                else {
                    window.location.href = "/";
                }
            }
        });
    }

    $("#loginBtn").click(function(){
        var _username = $("#username").val();
        var _password = $("#password").val();
        $.ajax({
            url: "/login",
            type: "post",
            dataType: "json",
            headers: {"token": ""},
            data:{"username": _username, "password": _password},
            success: function(data){
                console.log(String(data.status));
                if (String(data.status) == "success") {
                    localStorage.setItem("token", data.token);
                    window.location.href = "/index";
                }
                else if (String(data.status) == "fail") {
                    $("#logintext").text(String(data.info));
                    localStorage.removeItem("token");
                }
                else {
                    //alert("登录失败！用户名或密码错误！");
                    $("#logintext").text("发生错误：" + String(data.info));
                    localStorage.removeItem("token");
                }
            }
        });
    });
});