function MyForgot() {
    var oError=document.getElementById("error_box")
    var oEmail=document.getElementById("email").value
    var regEmail = /^[A-Za-z\d]+([-_.][A-Za-z\d]+)*@([A-Za-z\d]+[-.])+[A-Za-z\d]{2,4}$/;

    oError.innerHTML=""
    if (!regEmail.test(oEmail)) {
        oError.innerHTML = "邮箱账号格式有误";
        return false;
    }
}