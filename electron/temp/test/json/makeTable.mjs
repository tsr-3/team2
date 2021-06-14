function maketable(gakusei_list){
  // この部分に表を作るやつ書いて
  // jsonから読み取ったobjectはgakusei_listに入れたから
  let body = document.querySelector("body");//bodyに入れたい

  let table = document.createElement("table");
  let tableBody = document.createElement("tbody");

  let object_keys = Object.keys(gakusei_list[0]);//この書き方よろしくない気がする

  for (let i = 0; i < gakusei_list.length; i++){
    let row = document.createElement("tr");

    for (let j = 0; j < object_keys.length; j++){
      let cell = document.createElement("td");
      let cellText = document.createTextNode(gakusei_list[i][object_keys[j]]);
      cell.appendChild(cellText);
      row.appendChild(cell);
    }

    tableBody.appendChild(row);
  }

  table.appendChild(tableBody);
  body.appendChild(table);
  table.setAttribute("border", "2");
}