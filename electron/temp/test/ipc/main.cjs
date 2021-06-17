// main process

const { ipcMain } = require('electron');
const electron = require('electron');

ipcMain.on('calc_add', (event, args)=>{
  event.returnValue = {message: args.message[0] + args.message[1]};
});
