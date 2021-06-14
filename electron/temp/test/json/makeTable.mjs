function maketable(gakusei_list){
  // この部分に表を作るやつ書いて
  // jsonから読み取ったobjectはgakusei_listに入れたから
  let body = document.querySelector("body");//bodyに入れたい

  let table = document.createElement("table");
  let tableBody = document.createElement("tbody");
  //console.log(gakusei_list.length);

  //console.log(gakusei_list)

  for (let i = 0; i < gakusei_list.length; i++){
    let row = document.createElement("tr");

    let object_keys = Object.keys(gakusei_list[i]);
    //console.log(object_keys);//1からn人までの数値

    for (let j = 0; j < object_keys.length; j++){
      let object_keys_keys = object_keys[j];//各キーの中のキーを取得
      console.log(object_keys_keys); // => 学籍番号，名前，ふりがな，性別，IDm が出る
      //console.log(gakusei_list[i].object_keys_keys);

      let cell = document.createElement("td");
      let cellText = document.createTextNode(gakusei_list[i][object_keys_keys]);
      cell.appendChild(cellText);
      row.appendChild(cell);
    }

    tableBody.appendChild(row);
  }

  table.appendChild(tableBody);
  body.appendChild(table);
  table.setAttribute("border", "2");
}