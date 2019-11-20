
$(document).ready(function () {
    if (verify_token() == "error") {
        window.location.href = "/login";
    }
});

//$(function() {
//    $(document).ready(function () {
//        if (verify_token() == "error") {
//            window.location.href = "/login";
//        }
//    });
//});



