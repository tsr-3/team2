// main process of electron

const electron = require('electron');
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;

let mainWindow = null;

app.on('ready', ()=>{
  mainWindow = new BrowserWindow({
    width: 720,
    height: 480,
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: false,
      preload: __dirname + '/preload.cjs'
    }
  });
  mainWindow.loadURL('file://' + __dirname + '/renderer/index.html');
  // mainWindow.webContents.openDevTools();
  mainWindow.on('closed', ()=>{
    mainWindow = null;
  });
});

// ref: https://qiita.com/umamichi/items/6ce4f46c1458e89c4cfc

// load ipc-module
require('./communicate.main.cjs');
