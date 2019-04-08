function myLogin() {
    var oUname=document.getElementById("name")
    var oEmail=document.getElementById("email").value
    var oPass=document.getElementById("password")
    var oPas=document.getElementById("re-password")
    var oError=document.getElementById("error_box")
    var regEmail = /^[A-Za-z\d]+([-_.][A-Za-z\d]+)*@([A-Za-z\d]+[-.])+[A-Za-z\d]{2,4}$/;

    oError.innerHTML=""
    if(oUname.value.length<5||oUname.value.length>20){
        oError.innerHTML='请输入6-20位的用户名'
        return false;

    }
    else if(oUname.value.charCodeAt(0)>=48&&oUname.value.charCodeAt(0)<=57){
        oError.innerHTML='用户名首字母不能为数字'
        return false;
    }
    else if (!regEmail.test(oEmail)) {
        oError.innerHTML = "邮箱账号格式有误";
        return false;
    }
    else if(oPas.value!=oPass.value){
        oError.innerHTML='密码输入不一致，请重新输入'
        return false
    }
    else if(oPass.value.length<6||oPass.value.length>20){
        oError.innerHTML='请输入6-20位的密码'
        return false;
    }
    else{
        window.location.href="login.html"
    }
}



// //验证用户名
// function check_userName() {
//     var userName = document.getElementById("name").value;
//     var regName = /[a-zA-Z]\w{4,16}/
//     if (userName == "" || userName.trim() == "") {
//       document.getElementById("err_name").innerHTML = "请输入用户名";
//       return false;
//     }
//     else if (!regName.test(userName)) {
//       document.getElementById("err_name").innerHTML = "由英文字母和数字组成的4-16位字符，以字母开头";
//       return false;
//     }
//     else {
//       document.getElementById("err_name").innerHTML = "ok!!!";
//       return true;
//     }
//   }
//   //验证邮箱
// function check_email() {
//     var email = document.getElementById("email").value;
//     var regEmail = /^\w+@\w+((\.\w+)+)$/;
//     if (email == "" || email.trim() == "") {
//       document.getElementById("err_email").innerHTML = "请输入邮箱";
//       return false;
//     }
//     else if (!regEmail.test(email)) {
//       document.getElementById("err_email").innerHTML = "邮箱账号@域名。如good@tom.com、whj@sina.com.cn";
//       return false;
//     }
//     else {
//       document.getElementById("err_email").innerHTML = "ok!!!";
//       return true;
//     }
//   }
//   //验证密码
//   function check_pwd() {
//     var pwd = document.getElementById("password").value;
//     var regPwd = /^\w{4,10}$/;
//     if (pwd == "" || pwd.trim() == "") {
//       document.getElementById("err_pwd").innerHTML = "请输入密码";
//       return false;
//     } else if (!regPwd.test(pwd)) {
//       document.getElementById("err_pwd").innerHTML = "格式错误";
//       return false;
//     } else {
//       document.getElementById("err_pwd").innerHTML = "ok!!!";
//       return true;
//     }
//   }
//   //确认密码
//   function check_pwd2() {
//     var pwd = document.getElementById("password").value;
//     var pwd2 = document.getElementById("re-password").value;
//     if (pwd2 == "" || pwd2.trim() == "") {
//       document.getElementById("err_pwd2").innerHTML = "请输入密码";
//       return false;
//     } else if (!pwd2.equals(pwd)) {
//       document.getElementById("err_pwd2").innerHTML = "两次输入密码不一致";
//       return false;
//     } else {
//       document.getElementById("err_pwd2").innerHTML = "ok!!!";
//       return true;
//     }
//   }