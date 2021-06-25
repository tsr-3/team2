# electron

## 現時点でのtsr担当分の最新スクリプト

実行時のnode.js (node_modules) とかは自分で入れてください

---

## ファイル名と内容の対応について
---
**html編**
### ログイン前部分
- index.html
>electronを立ち上げて最初に表示される画面
- login.html
>ユーザがログインをするための画面(tsr担当ではないため仮置き)
- createaccount.html
>ユーザアカウント作成用のフォーム
### ログイン後部分
- menu.html
>ユーザが利用できる機能メニューを表示する<br>
改善案があったらください
- makelist.html
>出席を判定するためのjsonファイルを作成するフォーム<br>
最終的にはフォームにはjsonとかなんとか書かなくしてDDエリアと時間設定だけにするつもり
- readjson.html
>出席状況取得後のjsonファイルを読み取るための部分<br>
これもmakelist同様
- graph.html
>読み取った出席状況をグラフ化して表示する<br>
方法模索中
- newWindowTest.html
>名前の通り，テスト用です．最終的には消えて無くなります．
---
**JavaScript編**
- main.js
>electronアプリ起動用です．特にいじることはありませんが，まだ改善は可能です．
- csvToJson.mjs
>CSV形式からjson形式に変換するスクリプト(仮置き)<br>
hatena氏が作っている方が最終版になる予定
- makeTable.mjs
>オブジェクトを受け取って表を作成するスクリプト
- makeGraph.mjs
>オブジェクトを受け取ってグラフ化するスクリプト<br>
グラフ化の方法は模索中
- createNewWindow.js
>相対パス(テキスト)を引数に新しいウィンドウを表示する
- printPDF.mjs
>画面上の表示をPDF印刷するスクリプト<br>
やり方模索中
---
**css編**
- test.css
>testって言う名前だけど現在これしかないcss
---
**json編**
- package.json
>electronパッケージの設定ファイル<br>
特にいじる必要は無い
---
**その他**
- README.md
>これ．気が向いたら更新する．
- TODO
>ToDoリスト<br>
拡張機能"todo+"を入れるとチェックが入れられるようになる