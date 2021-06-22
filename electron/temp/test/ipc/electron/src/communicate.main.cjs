// internal process communication

const electron = require('electron');

electron.ipcMain.on('calc_add', (event, arg)=>{
  event.returnValue = {message: arg.message[0] + arg.message[1]};
});
