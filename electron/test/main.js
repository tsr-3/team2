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
    mainWindow = new BrowserWindow({width: 800, height: 600});
    mainWindow.loadFile('./index.html');
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
      label: 'メニュー',
      submenu: [
        {
          label: 'メインページ',
          click () { mainWindow.loadURL(`file://${__dirname}/index.html`); }
        },{
          label: '成績表示',
          click () { mainWindow.loadURL(`file://${__dirname}/sub.html`); }
        },{
          label: 'json作成ツール',
          click () { mainWindow.loadURL(`file://${__dirname}/makelist.html`); }
        }
      ]
    },{
      label: 'Webbb',
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
      label: '印刷(未実装)',
      submenu: [
        {
          label: '印刷',
          click() { window.print();}
        }
      ]
    }
  ]

  const menu = Menu.buildFromTemplate(template)
  Menu.setApplicationMenu(menu)
}
