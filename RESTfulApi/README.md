# RESTful服务器：http://host:port/api

## 所有用户角色及其权限：

`root`
```
除了最自己删、改、查。拥有一切权限（只要存在该功能）。
```

`admin`
```
除了对于root用户的一切操作，对同等级角色的删除与更改。拥有一切权限，具体如下：
    用户：
        1、获取非root用户列表（含过滤）。
        2、创建用户（可创建admin/stuff两种角色的用户）。
        3、删除stuff用户。
        4、更新stuff和自己的资料。
        5、查看非root用户的详情信息。
    图书：
        1、获取图书列表（含过滤）。
        2、增加图书。
        3、下架图书。
        4、更新图书信息。
        5、查看图书详情信息。
    书种：
        1、获取书种（含过滤）。
        2、增加书种。
        3、删除书种（前提是无图书引用该书种）。
        4、查看书种详情信息。
    索引：
        1、查看引用某书种的所有书籍。
        2、解除所有书籍对某书种的引用（之后可以删除）。
        3、查看与某用户相关的所有销售记录。
        4、查看与某图书有关的所有销售记录。
        5、查看与某VIP有关的所有销售记录。
    销售记录：
        1、获取所有销售记录。
        2、查看某销售记录详情。
        3、增加销售记录（即售书）。
    VIP：
        1、获取VIP列表（含过滤）。
        2、创建VIP。
        3、获取VIP详情信息。
        4、删除某VIP。
```

`stuff`
```
普通员工的权限，具体如下：
    用户：
        1、获取角色为stuff用户列表（含过滤）。
        2、更新自己的资料。
        5、查看角色为stuff用户的详情信息。
    图书：
        1、获取图书列表（含过滤）。
        2、查看图书详情信息。
    书种：
        1、获取书种（含过滤）。
        2、增加书种。
        3、查看书种详情信息。
    索引：
        1、查看引用某书种的所有书籍。
        2、查看与某用户相关的所有销售记录。
        3、查看与某图书有关的所有销售记录。
        4、查看与某VIP有关的所有销售记录。
    销售记录：
        1、增加销售记录（即售书）。
    VIP：
        1、获取VIP列表（含过滤）。
        2、创建VIP。
        3、获取VIP详情信息。
        4、删除某VIP。
```

## 所有接口地址及其简略：
  
`/session` *登录、注销*

`/accounts` *获取用户、新增用户*
`/accounts/<account_id>` *用户删、改、查*

`/books` *获取图书、新增图书*
`/books/<book_id>` *图书删、改、查*

`/vips` *获取VIP、新增VIP*
`/vips/<vip_id>` *VIP删、改、查*

`/types` *获取书种、新增书种*
`/types/<book_type_id>` *书种删、改、查*

`/sales_records` *获取销售记录、添加销售记录*
`/sales_records/<sales_record_id>` *销售记录删、查*

`/references/book2type/<book_type_id>` *解除图书对书种的索引、获取某书种的所有图书*
`/references/record2account/<account_id>` *获取某用户的售书记录*
`/references/record2book/<book_id>` *获取某图书的销售记录*
`/references/record2vip/<vip_id>` *获取某VIP的购买记录*


## 详情说明

### /session 登录、注销 

#### post: 登录
##### form-data
```
username: yangjing
password: secret
```
##### response
```
{
  "message": null,
  "token": "Tj34pi7kbNi5f8t6"
}

Tip: message若不为null，则创建失败，此时token为null
```

#### delete: 登出
##### headers
```
token: DVh64CUJFBq8xnrO
```
<font color=red>注：如无特别说明，以下所有请求除了要求的form-data或param以外，还要必须提供key为\'token'值为\'XXXX'的header键值对。根据RESTful的等幂性，此字段提供身份验证。</font>
##### response
```
1 or 0

Tip: 为1表示成功登出, 0表示已经登出
```

### /accounts 获取用户、新增用户

#### get 获取所有用户
##### param(可选，此时表示过滤) 
```
/accounts?username=skyduy&&nickname=于俊

Tip: 仅有两个有效参数：username nickname
```
##### response
```
{
  "accounts": [
    {
      "created": "Fri, 18 Mar 2016 15:05:47 -0000",
      "description": "",
      "id": "56eba8cb159ce124604403e2",
      "nickname": "于俊",
      "role": "stuff",
      "username": "skyduy"
    },
    {
      "created": "Fri, 18 Mar 2016 15:05:54 -0000",
      "description": "",
      "id": "56eba8d2159ce124604403e4",
      "nickname": "杨靖",
      "role": "stuff",
      "username": "yangjing"
    }
  ]
}
```
#### post 新增用户
##### form-data
```
username: skyduy
nickname: 杨靖
password: secret
confirm: secret
role: 0 (其中0为员工，1为超级管理员)
```
##### response
```
{
  "message": null,
  "token": "Tj34pi7kbNi5f8t6"
}

Tip: message若不为null，则创建失败，此时token为null
```

### /accounts/<account_id\> 用户删、改、查

#### get 查看用户详情信息
```
todo
```

### /books 获取图书、新增图书

#### get 获取图书列表（含过滤）
```
todo
```

### /books/<book_id\> 图书删、改、查

#### get 查看图书详情信息
```
todo
```

### /vips 获取VIP、新增VIP

#### get 获取VIP列表（含过滤）
```
todo
```

### /vips/<vip_id\> VIP删、改、查

#### get 查看某VIP详情信息
```
todo
```

### /types 获取书种、新增书种

#### get 获取书种列表（含过滤）
```
todo
```

### /types/<book_type_id\> 书种删、改、查

#### get 查看某书籍详情信息
```
todo
```

### /sales_records 获取销售记录、添加销售记录

#### get 获取销售记录列表
```
todo
```

### /sales_records/<sales_record_id\> 销售记录删、查

#### get 查看销售记录详情信息
```
todo
```

### /references/book2type/<book_type_id\> 解除图书对书种的索引、获取某书种的所有图书

#### get 获取某书种所有图书
```
todo
```

### /references/record2account/<account_id\> 获取某用户的售书记录

#### get 获取某用户售书记录
```
todo
```

### /references/record2book/<book_id\> 获取某图书的销售记录

#### get 获取某图书的销售记录
```
todo
```

### /references/record2vip/<vip_id\> 获取某VIP的购买记录

#### get 获取某VIP的购买记录
```
todo
```

### TODO