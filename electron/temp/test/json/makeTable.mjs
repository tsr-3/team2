function maketable(append_list,filename){
  // この部分に表を作るやつ書いて
  // jsonから読み取ったobjectはgakusei_listに入れたから

  //オブジェクトのキー(gakusei_listの場合)
  let object_keys = Object.keys(append_list[0]);//この書き方よろしくない気がする

  let body = document.querySelector("body");//bodyに入れたい

  let table = document.createElement("table");
  let caption = document.createElement("caption");
  let table_title = document.createTextNode(filename);
  caption.appendChild(table_title);
  table.appendChild(caption);
  let thead = document.createElement("thead");
  let tr = document.createElement("tr");
  for (let i = 0; i < object_keys.length; i++){
    let th = document.createElement("th");
    let subtitle = document.createTextNode(object_keys[i]);
    th.appendChild(subtitle);
    tr.appendChild(th);
  }
  thead.appendChild(tr);
  table.appendChild(thead);
  let tableBody = document.createElement("tbody");

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
  table.setAttribute("border", "1");
}