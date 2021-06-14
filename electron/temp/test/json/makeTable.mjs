function maketable(gakusei_list){
  // この部分に表を作るやつ書いて
  // jsonから読み取ったobjectはgakusei_listに入れたから
  let body = document.getElementsByTagName("body")[0];

  let tbl = document.createElement("table");
  let tblBody = document.createElement("tbody");

  for (let i = 0; i < gakusei_list.length; i++){
    let row = document.createElement("tr");

    for (let j = 0; j < gakusei_list[0].length; j++){
      let cell = document.createElement("td");
      let cellText = document.createTextNode(gakusei_list[i][j]);
      cell.appendChild(cellText);
      row.appendChild(cell);
    }

    tblBody.appendChild(row);
  }

  tbl.appendChild(tblBody);
  body.appendChild(tbl);
  tbl.setAttribute("border", "2");
}