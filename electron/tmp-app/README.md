# electron

## 現時点でのtsr担当分の最新スクリプト

実行時のnode.js (node_modules) とかは自分で入れてください

---

## ファイル名と内容の対応について
**html編**
### ログイン前部分
- index.html
>electronを立ち上げて最初に表示される画面
- login.html
>ユーザがログインをするための画面(担当ではないため仮置き)
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
