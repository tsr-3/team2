/**
 * @param filepath:str
 * @return {undefined}
 */
/*
  入力：ファイルの相対パスを文字列で入力
  出力：別ウィンドウで指定されたページを開く
  説明：新しいウィンドウを作成して，指定されたページを開くスクリプト

*/

function openNewWindow(filepath) {
  //const url = 'newWindowTest.html'
  window.open(filepath, '', { width: 800, height: 600 })
}