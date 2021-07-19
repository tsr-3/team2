

async function createLecttime() {
  let starttime = document.querySelector('form > input#starttime').value;
  let attendtime = document.querySelector('form > input#attendtime').value;
  let latenesstime = document.querySelector('form > input#latenesstime').value;

  await csvFileReader();
  // テスト用
  if (starttime == null || starttime == undefined || starttime == '') {
    console.log("講義開始時間は入力しよう...うん...");
  } else {
    console.log(starttime);
  }
  if (attendtime == null || attendtime == undefined || attendtime == '') {
    console.log("出席受付時間入力よろ");
  } else if (attendtime < 0){
    console.log('出席受付時間は0以上で入力してください');
  }
  if (latenesstime == null || latenesstime == undefined || latenesstime == '') {
    console.log("遅刻受付時間入力はよ");
  } else if (latenesstime < 0){
    console.log('遅刻受付時間は0以上で入力してください');
  }

  let lecttime = { 'start': starttime, 'attend': attendtime, 'lateness': latenesstime }; // 講義に関する時間

  return lecttime
};

function csvFileReader() {
  let csvpath = document.querySelector('#csv-reader').value;
  if (!csvpath.slice(4-csvpath.length).match(/.csv/)) {
    return;
  }


}

function csv2json(csvArray){
  let jsonArray = [];

  // 1行目から「項目名」の配列を生成する
  let items = csvArray[0].split(',');

  // CSVデータの配列の各行をループ処理する
  // 配列の先頭要素(行)は項目名のため処理対象外
  // 配列の最終要素(行)は空のため処理対象外
  for (let i = 1; i < csvArray.length; i++) {
    let a_line = new Object();
    // カンマで区切られた各データに分割する
    let csvArrayD = csvArray[i].split(',');
    // 各データをループ処理する
    for (let j = 0; j < items.length; j++) {
      // 要素名：items[j]
      // データ：csvArrayD[j]
      a_line[items[j]] = csvArrayD[j];
    }
    jsonArray.push(a_line);
  }
  return jsonArray;
}