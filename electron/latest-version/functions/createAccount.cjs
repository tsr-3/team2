/**
 * @param {undefined}
 *
 * @return {{ID:string, passwd:string}} after
 */
const SaveDataFile = require('./AES256CBC/readDataFromFile')

function createAccount() {
  let ID = document.querySelector('form > input#ID').value;
  let passwd = document.querySelectorAll('form > input#passwd')[0].value;
  let re_passwd = document.querySelectorAll('form > input#passwd')[1].value;

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
  if (re_passwd == null || re_passwd == undefined || re_passwd == '') {
    console.log("パスワード再入力はよ");
  } else {
    console.log(re_passwd);
  }
  if (passwd != re_passwd) {
    console.log("パスワードが一致しないでござる");
  }

  SaveDataFile


};
