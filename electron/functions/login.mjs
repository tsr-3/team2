// ログイン処理は廃止した

/**
 * @param {undefined}
 *
 * @return {{ID:string, passwd:string}} after
 */

function login() {
  let ID = document.querySelector('form > input#ID').value;
  let passwd = document.querySelector('form > input#passwd').value;
  // テスト用
  if (ID == null || ID == undefined || ID == '') {
    console.log("IDは入力しよう...うん...");
  } else {
    console.log(ID);
  }
  if (passwd == null || passwd == undefined || passwd == '') {
    console.log("パスワード入力よろ");
  } else {
    console.log(passwd);
  }

  // ログイン判定ってどこのデータと照らし合わせればいいんだろ？
  // ユーザが触れないようなところに保存しておく方がよさそうね
  // 暗号化呼び出し(どれ呼び出すのじゃ？)
  /*if(passwd != aes256.cjs -> dec(保存済みpasswd)){
    console.log("せんせ～ぱすわーど一致しないよ？");
  } else {
    //mainWindow.location.href = '../pages/mainmenu.html';
  }*/
}