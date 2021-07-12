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
  mainWindow.loadURL('file://' + __dirname + '/pages/index.html');
    // ウィンドウメニューをカスタマイズ
    initWindowMenu();

// ウィンドウが閉じられたらアプリも終了
    mainWindow.on('closed', function() {
        mainWindow = null;
    });
});

// メニューバーを変更する
function initWindowMenu(){
  const template = [
    {
      label: 'メニュー',
      submenu: [
        {
          label: 'スタート画面',
          click () { mainWindow.loadURL(`file://${__dirname}/pages/index.html`); }
        },{
          label: '出席状況確認ツール',
          click () { mainWindow.loadURL(`file://${__dirname}/pages/check-attendance.html`); }
        },{
          label: '履修者リスト作成ツール',
          click () { mainWindow.loadURL(`file://${__dirname}/pages/create-lectinfo.html`); }
        }
      ]
    },{
      label: 'ヘルプ',
      submenu: [
        {
          label: '操作方法ヘルプ',
          accelerator: switchCharactersByOS('Command+H', 'Ctrl+H'),
          click() {
            subWindow = new BrowserWindow({ width: 800, height: 600 });
            subWindow.loadURL(`file://${__dirname}/pages/help.html`);
          }
        }
      ]
    },{
      label: '終了',
      submenu: [
        {
          label: '終了',
          accelerator: switchCharactersByOS('Command+Q', 'Ctrl+Q'),
          click() { app.quit(); }
        }
      ]
    }
  ]

  const menu = Menu.buildFromTemplate(template)
  Menu.setApplicationMenu(menu)
}

/*
  WindowsとMacで文字を切り替える
*/
 function switchCharactersByOS(forMac, forWin) {
  if (process.platform == 'darwin') {
    return forMac;
  }
  return forWin;
};