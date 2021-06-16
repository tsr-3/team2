const electron = require('electron');
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;

let mainWindow = null;
app.on('ready', () => {
  // mainWindowを作成（windowの大きさや、Kioskモードにするかどうかなどもここで定義できる）
  mainWindow = new BrowserWindow({ width: 600, height: 400 });
  // Electronに表示するhtmlを絶対パスで指定（相対パスだと動かない）
  // 絶対パス指定は以下の方法で決定させる
  mainWindow.loadURL(`file://${__dirname}/index.html`);

  mainWindow.on('closed', function() {
    mainWindow = null;
  });
});