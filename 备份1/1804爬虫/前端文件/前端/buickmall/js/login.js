function MyLogin() {
    var username = document.getElementById('username')
    var password = document.getElementById('password')
    var login = document.getElementById('login')
    var oError=document.getElementById("error_box")

    oError.innerHTML=""
    if(username.value.length<5||username.value.length>20){
        oError.innerHTML='请输入6-20位的用户名'
        return false;
    }
    else if(password.value.length<6||password.value.length>20){
        oError.innerHTML='请输入6-20位的密码'
        return false;
    }
    else{
        window.location.href="index.html"
    }
}







// var username = document.getElementById('username')
// var password = document.getElementById('password')
// var login = document.getElementById('login')
// login.onclick=function(form){
//     if(username.value==""){
//         alert('账号不能为空！')
//         return false
//     }
//     else if(password.value==""){
//         alert('密码不能为空！')
//         return false
//     }
//     else{
//         window.location.href="index.html"
//     }
// }
