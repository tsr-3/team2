/**
 *
 * @param {object} append_list :object
 * @param {string} filename :str
 */

function maketable(append_list, filename) {
  // この部分に表を作るやつ書いて -> 書いた
  // jsonから読み取ったobjectはgakusei_listに入れたから ->　append_list(和訳：出席リスト)とfilenameを入れるように改造したぞ(jsonToObject.mjsの方も)

  //オブジェクトのキーの中のキー(gakusei_listの場合，学籍番号，名前，ふりがな，性別，IDm)を取得
  let object_keys = Object.keys(append_list[0]);//この書き方よろしくない気がするのでhatena氏のコメント待ち

  let body = document.querySelector("body");//<body></body>に表を入れる

  let table = document.createElement("table");//<table>を作成
  let caption = document.createElement("caption");//<caption>を作成
  let table_title = document.createTextNode(filename);//<caption>filename</caption>にする
  caption.appendChild(table_title);
  table.appendChild(caption);

  //オブジェクトのキーを見出しにする処理
  let thead = document.createElement("thead");//<thead>を作成
  let tr = document.createElement("tr");//<tr>を作成
  for (let i = 0; i < object_keys.length; i++){
    let th = document.createElement("th");//<th>を作成
    let subtitle = document.createTextNode(object_keys[i]);
    th.appendChild(subtitle);
    tr.appendChild(th);
  }
  thead.appendChild(tr);
  table.appendChild(thead);
  let tableBody = document.createElement("tbody");
  //見出しの作成終了

  //ここから内容の描画だよ
  for (let i = 0; i < append_list.length; i++){
    let row = document.createElement("tr");

    for (let j = 0; j < object_keys.length; j++){
      let cell = document.createElement("td");
      let cellText = document.createTextNode(append_list[i][object_keys[j]]);
      cell.appendChild(cellText);
      row.appendChild(cell);
    }

    tableBody.appendChild(row);
  }
  table.appendChild(tableBody);
  body.appendChild(table);
  //内容の表示終了

  table.setAttribute("border", "1");//よく分からんけど，表とページの境界の線を設定できるらしい
}