# Бары Москвы

Скрипт ищет по файлу с с данными в формате json, загруженному из базы [data.mos.ru](https://data.mos.ru/) бары с максимальным и минимальным количеством посадочных мест, а также находит ближайший бар по заданным пользователем координатам

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5 и файла с данными в формате json, например:

```
{
  "features": [{
    "geometry": {
      "coordinates": [37.621587946152012, 55.765366956608361],
      "type": "Point"
    },
    "properties": {
      "DatasetId": 1796,
      "VersionNumber": 2,
      "ReleaseNumber": 2,
      "RowId": "20a0b7c9-dad3-4af8-a2a2-08170f74379b",
      "Attributes": {
        "global_id": 20660594,
        "Name": "Юнион Джек",
        "IsNetObject": "нет",
        "OperatingCompany": null,
        "AdmArea": "Центральный административный округ",
        "District": "Мещанский район",
        "Address": "Нижний Кисельный переулок, дом 3, строение 1",
        "PublicPhone": [{
          "PublicPhone": "(495) 621-19-63"
        }],
        "SeatsCount": 30,
        "SocialPrivileges": "нет"
      }
    },
    "type": "Feature"
  },
```

пример результата работы


```#!bash

$ python bars.py <filename>

The biggest bar: Спорт бар «Красная машина», 450 seats
The smallest bar: Бар «ФОРМУЛА КИНО», 1 seats
Your longitude:37.6215879
Your latitude:55.765366
The closest bar: Юнион Джек

```


# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
