$(document).ready(function() {
    $("#menu-0-3").addClass("dropdown-toggle");
    if (verify_token() == "error") {
        window.location.href = "/login";
    }
});
