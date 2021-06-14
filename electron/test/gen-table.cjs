//表を動的に作成してGUIに表示するためのスクリプト
//テスト的にコピーしたままの状態
//コピー元URL：https://developer.mozilla.org/ja/docs/Web/API/Document_Object_Model/Traversing_an_HTML_table_with_JavaScript_and_DOM_Interfaces

//jsonを読み取るスクリプトをこの中か別ファイルに追加して，generate-tableの引数にjsonデータ，データ配列の縦横幅を入れて，順番に表示する感じ
//今後の展望的に，別ファイルで関数的に作っていった方が作業しやすいかな？


function generateTable() {

  // get the reference for the body
  var body = document.getElementsByTagName("body")[0];

  // creates a <table> element and a <tbody> element
  var tbl = document.createElement("table");
  var tblBody = document.createElement("tbody");


  //ここからjson読み込みとその他諸々

  // const fs = require('fs');

  // let attendData = JSON.parse(fs.readFileSync('./gakusei-list.json', 'utf8'));
  //ここまで


  // creating all cells
  // 人数でも指定すればいいと思われる
  for (var i = 0; i < 100; i++) {
    // creates a table row
    var row = document.createElement("tr");

    // ここで横に何個列ができるかを指定できる つまり要素を書いていくところになる
    // オブジェクトの添え字をjとして指定できれば完成に近づくかな
    for (var j = 0; j < 1; j++) {
      // Create a <td> element and a text node, make the text
      // node the contents of the <td>, and put the <td> at
      // the end of the table row
      var cell = document.createElement("td");
      var cellText = document.createTextNode(attendData[i]);
      cell.appendChild(cellText);
      row.appendChild(cell);
    }

    // add the row to the end of the table body
    tblBody.appendChild(row);
  }

  // put the <tbody> in the <table>
  tbl.appendChild(tblBody);
  // appends <table> into <body>
  body.appendChild(tbl);
  // sets the border attribute of tbl to 500;
  tbl.setAttribute("border", "500");
}