// preload

window.electron = require('electron');

// kill ctrl+shift+i / f12 (kill dev tool)
document.addEventListener('keydown', event=>{
  if(event.key.toLowerCase() == 'f12' || event.key.toLowerCase() == 'i' && event.shiftKey && event.ctrlKey){
    console.log('ctrl + shift + i');
    event.preventDefault();
  }
  console.log(event.key.toLowerCase());
});
