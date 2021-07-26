/**
 * @param filepath:str
 * @return {undefined}
 */
/*
  入力：ファイルの相対パスを文字列で入力
  出力：指定されたパスのページを別ウィンドウで開く
  説明：新しいウィンドウを作成して，指定されたページを開くスクリプト
*/

function openNewWindow(filepath) {
  window.open(filepath, '', { width: 800, height: 600 })
}