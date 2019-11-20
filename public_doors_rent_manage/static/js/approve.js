$(document).ready(function() {
    $("#huiche").hide();
    $("#h-apply-id").hide();
    var mode = $("#mode").val();
    if (mode == "search") {
        $("#btn-show-approve").hide();
    }
    var unit_pro = "";
    if ($("#unit-pro-business").text() == "1") {
        unit_pro += "企业；";
    }
    if ($("#unit-pro-office").text() == "1") {
        unit_pro += "机关事业单位；";
    }
    if ($("#unit-pro-employment").text() == "1") {
        unit_pro += "个体工商户；";
    }
    if ($("#unit-pro-retire").text() == "1") {
        unit_pro += "离退休；";
    }
    if ($("#unit-pro-other").text() == "1") {
        unit_pro += "其它；";
    }
    $("#td-unit-pro").text(unit_pro);
    var pro = "";
    if ($("#pro-graduate").text() == "1") {
        pro += "新就业普通高校毕业生；";
    }
    if ($("#pro-outside").text() == "1") {
        pro += "外来务工人员；";
    }
    if ($("#pro-gov-talent").text() == "1") {
        pro += "政府引进特殊人才；";
    }
    if ($("#pro-difficult").text() == "1") {
        pro += "困难家庭；";
    }
    if ($("#pro-cheap").text() == "1") {
        pro += "廉租房保障家庭；";
    }
    if ($("#pro-economy").text() == "1") {
        pro += "经济房保障家庭；";
    }
    $("#td-pro").text(pro);
    if (verify_token() == "error") {
        window.location.href = "/login";
    }
});
/*
保存申请审批表到pdf
*/
$.save_table = function() {
    $("#huiche").show();
    var target = document.getElementById("pdf-info");
    target.style.background = "#FFFFFF";
    var apply_id = $("#apply-id").val();
    html2canvas(document.getElementById("pdf-info")).then (canvas => {
        var contentWidth = canvas.width;
        var contentHeight = canvas.height;
        //一页pdf显示html页面生成的canvas高度;
        var pageHeight = contentWidth / 592.28 * 841.89;
        //未生成pdf的html页面高度
        var leftHeight = contentHeight;
        //页面偏移
        var position = 0;
        //a4纸的尺寸[595.28,841.89]，html页面生成的canvas在pdf中图片的宽高
        var imgWidth = 595.28;
        var imgHeight = 592.28/contentWidth * contentHeight;
        var pageData = canvas.toDataURL('image/jpeg', 1.0);
        var pdf = new jsPDF('', 'pt', 'a4');
        //有两个高度需要区分，一个是html页面的实际高度，和生成pdf的页面高度(841.89)
        //当内容未超过pdf一页显示的范围，无需分页
        if (leftHeight < pageHeight) {
            pdf.addImage(pageData, 'JPEG', 0, 0, imgWidth, imgHeight );
        }
        else {
            while (leftHeight > 0) {
                pdf.addImage(pageData, 'JPEG', 0, position, imgWidth, imgHeight)
                leftHeight -= pageHeight;
                position -= 841.89;
                //避免添加空白页
                if(leftHeight > 0) {
                  pdf.addPage();
                }
            }
        }
        pdf.save(apply_id + ".pdf");
    });
};
/*
审批
*/
$.approve = function() {
    var mode = $("#mode").val();
    if (mode == "street") {
        $.approve_street()
    }
    else if (mode == "dept") {

    }
};
/*
街道审批
*/
$.approve_street = function() {
    var apply_id = $("#apply-id-approve").val();
    var street_approve_remark = $("#street-approve-remark").val();
    $.ajax({
        url: "/approve",
        type: "post",
        dataType: "json",
        headers: {
        "opt_type": "street_approve",
        "token": localStorage.getItem("token")
        },
        data: {
        "apply_id": apply_id,
        "street_approve_remark": street_approve_remark
        },
        success: function(data) {
            if (String(data.status) == "success") {
                alert("审批完成！");
                $.search_apply_table(apply_id, "street");
            }
            else if (String(data.status) == "expired") {
                alert(String(data.info));
                window.location.href = "/login";
            }
            else if (String(data.status) == "state") {
                alert(String(data.info));
                $.search_apply_table(apply_id, "street");
            }
            else if (String(data.status) == "street") {
                alert(String(data.info));
            }
            else {
                alert("街道审批失败！" + String(data.info))
            }
        }
    });
};
/*
局审批
*/
$.approve_dept = function() {
    var apply_id = $("#apply-id-approve").val();
    var street_approve_remark = $("#street-approve-remark").val();
    $.ajax({
        url: "/approve",
        type: "post",
        dataType: "json",
        headers: {
        "opt_type": "dept_approve",
        "token": localStorage.getItem("token")
        },
        data: {
        "apply_id": apply_id,
        "street_approve_remark": street_approve_remark
        },
        success: function(data) {
            if (String(data.status) == "success") {
                alert("审批完成！");
                $.search_apply_table(apply_id, "dept");
            }
            else if (String(data.status) == "expired") {
                alert(String(data.info));
                window.location.href = "/login";
            }
            else if (String(data.status) == "state") {
                alert(String(data.info));
                $.search_apply_table(apply_id, "dept");
            }
            else if (String(data.status) == "street") {
                alert(String(data.info));
            }
            else {
                alert("局审批失败！" + String(data.info))
            }
        }
    });
};
