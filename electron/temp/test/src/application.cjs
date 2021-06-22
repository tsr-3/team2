// application main process //

// use electron
const electron = require('electron');
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;

// ipcs
require('./ipc.cjs');

let mainWindow = null;

app.on('ready', async ()=>{
  mainWindow = new BrowserWindow({
    width: 1080,
    height: 720,
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: false,
      preload: __dirname + '/renderer/preload.cjs'
    }
  });

  mainWindow.loadURL('file://' + __dirname + '/renderer/index.html');

  // on debug
  mainWindow.webContents.openDevTools();

  mainWindow.on('closed', async ()=>{
    mainWindow = null;
  });
});
