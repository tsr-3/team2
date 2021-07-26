# electron

## 現時点での最新スクリプト
もう変更しないであろうファイルを入れておく

実行時のnode.js (node_modules) とかは自分で入れてください
入れ方はStartDocumentを参照

---
## ファイル構造

> latest-version
- functions
  - jsファイル群．
- pages
  - htmlファイルとか
- styles
  - cssファイル
- その他
  - その他上記のカテゴリーに属しないもの

---

## ファイル名と内容の対応について
---
**html編**
### ログイン前部分
> index.html
- electronを立ち上げて最初に表示される画面
> login.html
- ユーザがログインをするための画面(tsr担当ではないため仮置き)
> create-account.html
- ユーザアカウント作成用のフォーム
### ログイン後部分
> mainmenu.html
- ユーザが利用できる機能メニューを表示する
- 改善案があったらください
> create-lectinfo.html
- 出席を判定するためのjsonファイルとか講義に関するデータを作成するフォーム
- 最終的にはフォームにはjsonとかなんとか書かなくしてDDエリアと時間設定だけにするつもり
> check-attendance.html
- 出席状況取得後のjsonファイルを読み取るための部分
> graph.html
- 読み取った出席状況をグラフ化して表示する
- 方法模索中
- 現時点ではここにありません tmp-app を参照してください
---
**JavaScript編**
> main.js
- electronアプリ起動用です．特にいじることはありませんが，まだ改善は可能です．
> csvToJson.mjs
- CSV形式からjson形式に変換するスクリプト(仮置き)
- hatena氏が作っている方が最終版になる予定
> makeTable.mjs
- オブジェクトを受け取って表を作成するスクリプト
> makeGraph.mjs
- オブジェクトを受け取ってグラフ化するスクリプト
- グラフ化の方法は模索中
- 現時点ではここにありません tmp-app を参照してください
> createNewWindow.js
- 相対パス(テキスト)を引数に新しいウィンドウを表示する
> printPDF.mjs
- 画面上の表示をPDF印刷するスクリプト
- 現時点ではここにありません tmp-app を参照してください
やり方模索中
---
**css編**
> mainstyle.css
- mainstyleって言う名前だけど現在これしかないcss
---
**json編**
> package.json
- electronパッケージの設定ファイル
- 特にいじる必要は無い
---
**その他**
> README.md
- これ．気が向いたら更新する．
- なんかリンクになってるけど気にすんな
