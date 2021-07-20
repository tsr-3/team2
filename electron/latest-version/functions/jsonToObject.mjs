/*
  jsonファイルをオブジェクトに変換する関数
*/

var global = {};

// input file read
document.querySelector('#json-reader').addEventListener('change', async (event)=>{
  //console.log(event.path[0].value); // path
  if (!event.path[0].value.match(/.json$|.t2pecf$/)){ // is json
    document.querySelector('#filetype-check').innerText = 'invalid filetype "' + event.path[0].value.match(/\..+$/)[0] + '"';
    document.querySelector('#filetype-check').classList.add('error')
    return;
  }
  let filename = event.target.files[0].name;
  var reader = new FileReader();
  reader.onload = (event)=>{
    global.json = event.target.result;
    maketable(JSON.parse(event.target.result), filename);
    drawgraph(JSON.parse(event.target.result), filename);
  };
  reader.readAsText(event.target.files[0]);
});

