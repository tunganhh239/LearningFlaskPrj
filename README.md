# Quản lý và theo dõi chỉ số BMI của người dùng

### Danh sách thông tin người dùng

**URL** : `/person`

**Method** : `GET`

**Data**

```json
[
    {
        "id"        :   1,
        "name"      :   "Khoa",
        "address"   :   "Hai Phong",
        "height"    :   1.7,
        "weight"    :   70.0
    },
    {
        "id"        :   2,
        "name"      :   "Tung Anh",
        "address"   :   "Ha Noi",
        "height"    :   1.76,
        "weight"    :   75.0
    },
    {
        "id"        :   3,
        "name"      :   "Viet Anh",
        "address"   :   "Da Nang",
        "height"    :   1.7,
        "weight"    :   65.0
    }
]
```

### Get thông tin người dùng theo id

**URL** : `/person/<id>`

**Method** : `GET`

**Data**

```json
{
    "id":1,
    "name": "TungAnh",
    "address": "Ha Noi",
    "weight": 75,
    "height:: 1.76
}
```

### Get chỉ số BMI của người dùng theo id

**URL** : `/bmi/<id>`

**Method** : `GET`

**Data**

```json
{
    "id":1,
    "name": "TungAnh",
    "BMI": 20.59,
    "messs": "Binh thuong"
}
```



### Thêm thông tin người dùng theo id

**URL** : `/person/<id>`

**Method** : `POST`

**Data**

```json
{
    "name": "TungAnh",
    "address": "Ha Noi",
    "weight": 75,
    "height:: 1.76
}
```


### Sửa thông tin người dùng theo id

**URL** : `/person/<id>`

**Method** : `PUT`


### Xóa thông tin người dùng theo id

**URL** : `/person/<id>`

**Method** : `DELETE`




