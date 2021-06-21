// ipc functions

const electron = require('electron');
const {hash} = require('./hash.cjs');

electron.ipcMain.on('ping', (event, arguments)=>{
  event.returnValue = arguments;
});



// debug
electron.ipcMain.on('hash', (event, args)=>{
  switch(args.type){
    case 'sha256':
      event.returnValue = hash.sha256(args.text);
    case 'sha384':
      event.returnValue = hash.sha384(args.text);
    case 'sha512':
      event.returnValue = hash.sha512(args.text);
    default:
      event.returnValue = null;
  }
});
