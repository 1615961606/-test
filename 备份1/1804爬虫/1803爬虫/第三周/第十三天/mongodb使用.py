db.createUser({
    'user':,
    'pwd':,
    'roles':[{'role':'','db':''}]

})
在etc下配置mongod.conf 配置文件
开启安全认证

mongo -u 用户名 -p 密码 --authenticationDatabase admin