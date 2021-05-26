こうした方がいいとか何かが足らないとかあったら教えてほしい

- [filename].zip
  - students.json
  - professors.json
  - lecture.json
  - attendances.txt

students.json
```json
[
  {
    "id": "学籍番号",
    "name": "名字 名前",
    "card-id": "カードに書いてあるID(なんていうんだっけ)"
  },
  {}
]
```

professors.json
```json
[
  {
    "id": "悩み中",
    "name": "名字 名前",
    "pass": "ハッシュ化されたパスワード"
  },
  {}
]
```

lecture.json
```json
{
  "name": "講義名",
  "start": "Wed 20:30:00 GMT+0900 (JST)",
  "end": "Wed 22:00:00 GMT+0900 (JST)",
  "modify": [
    {
      "type": "cancel/add",
      "start": "2021-05-26 20:30:00 GMT+0900 (JST)",
      "end": "2021-05-26 22:00:00 GMT+0900 (JST)"
    }
  ],
  "students": [
    "B21P037",
    "B21P033",
    ""
  ]
}
```

attendants.txt
```txt
2021-05-27 00:33:52 B21P037
2021-05-27 00:34:05 B21P033
```
