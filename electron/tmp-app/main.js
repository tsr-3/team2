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
      label: 'メニュー',
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
      label: 'Print(unimplemented)',
      submenu: [
        {
          label: 'Print to PDF',
          acceletor: switchCharactersByOS('Command+P', 'Ctrl+P'),
          click: function () { printPDF(); }
        }
      ]
    },{
      label: 'Exit',
      submenu: [
        {
          label: 'exit app',
          accelerator: switchCharactersByOS('Command+Q', 'Ctrl+Q'),
          click() { app.quit(); }
        }
      ]
    }
  ]

  const menu = Menu.buildFromTemplate(template)
  Menu.setApplicationMenu(menu)
}

function printPDF(event) {
  let dir_home = process.env[process.platform == "win32" ? "USERPROFILE" : "HOME"];
  const pdfPath = require("path").join(dir_home, "Desktop");
  mainWindow.webContents.printToPDF({}, function(error, data) {
    if (error) throw error
    fs.writeFile(pdfPath, data, function(error) {
      if (error) {
        throw error
      }
      shell.openExternal('file://' + pdfPath)
      event.sender.send('wrote-pdf', pdfPath)
    })
  })
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