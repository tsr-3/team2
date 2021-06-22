// Electronのモジュール
const electron = require("electron");

// アプリケーションをコントロールするモジュール
const app = electron.app;
const Menu = electron.Menu;

// ウィンドウを作成するモジュール
const BrowserWindow = electron.BrowserWindow;

// メインウィンドウはGCされないようにグローバル宣言
let mainWindow;

// 全てのウィンドウが閉じたら終了
app.on('window-all-closed', function() {
    if (process.platform != 'darwin') {
        app.quit();
    }
});

// Electronの初期化完了後に実行
app.on('ready', function() {
    // メイン画面の表示。ウィンドウの幅、高さを指定できる
  mainWindow = new BrowserWindow({ width: 800, height: 600 });
  mainWindow.loadURL('file://' + __dirname + '/index.html');
    // ウィンドウメニューをカスタマイズ
    initWindowMenu();

// ウィンドウが閉じられたらアプリも終了
    mainWindow.on('closed', function() {
        mainWindow = null;
    });
});


function initWindowMenu(){
  const template = [
    {
      label: 'Menu',
      submenu: [
        {
          label: 'start page',
          click () { mainWindow.loadURL(`file://${__dirname}/index.html`); }
        },{
          label: 'show list',
          click () { mainWindow.loadURL(`file://${__dirname}/readjson.html`); }
        },{
          label: 'make json',
          click () { mainWindow.loadURL(`file://${__dirname}/makelist.html`); }
        }
      ]
    },{
      label: 'Web',
      submenu: [
        {
          label: 'Google',
          click () { mainWindow.loadURL('https://www.google.co.jp/'); }
        },{
          label: 'Yahoo',
          click () { mainWindow.loadURL('http://www.yahoo.co.jp/'); }
        }
      ]
    },{
      label: 'Print(unimplemented)',
      submenu: [
        {
          label: 'Print to PDF',
          click() { window.print();}
        }
      ]
    },{
      label: 'Exit',
      submenu: [
        {
          label: 'exit app',
          click() { app.quit(); }
        }
      ]
    }
  ]

  const menu = Menu.buildFromTemplate(template)
  Menu.setApplicationMenu(menu)
}
