var global = {};

// input file read
document.querySelector('#json-reader').addEventListener('change', async (event)=>{
  console.log(event.path[0].value); // path
  if(!event.path[0].value.match(/.json/)) return; // jsonかどうか
  var reader = new FileReader();
  reader.onload = (event)=>{
    global.json = event.target.result;
  };
  reader.readAsText(event.target.files[0]);
});