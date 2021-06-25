/**
 * make graph
 * @param {[{student: string, ratio: number}]} attenddata
 * @param filename:str
 * @return {undefined}
 */
function make_graph(attenddata, filename) {
  let hr = document.querySelectorAll("hr")[0];
  let figure = document.createElement("figure");
  figure.className = 'graph';
  let figcaption = document.createElement("figcaption");
  figcaption.className = 'graph-caption';
  figcaption.textContent = filename;
  figure.appendChild(figcaption);

  //テスト中
  let ul = document.createElement("ul");
  for (let i = 0; i < 10; i++){
    let li = document.createElement("li");
    for (let j = 0; j < 10; j++){

    }
  }


  hr.appendChild(figure);
}


let arr = [
  {student:'id', ratio: 99.8},
  {student:'id', ratio: 99.8},
  {student:'id', ratio: 99.8},
]
