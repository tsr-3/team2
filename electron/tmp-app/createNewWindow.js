/*
  入力：ファイルの相対パスを文字列で入力
  出力：別ウィンドウで指定されたページを開く
  説明：新しいウィンドウを作成して，指定されたページを開くスクリプト
*/

function openNewWindow(url) {
  //const url = 'newWindowTest.html'
  window.open(url, '', { width: 800, height: 600 })
}