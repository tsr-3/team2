//コピー元：http://lifelog.main.jp/wordpress/?p=2970

//mdn：https://developer.mozilla.org/ja/docs/Web/API/Blob

//ファイル出力：https://techacademy.jp/magazine/28206

//hatena氏のイベントハンドラを流用
document.querySelector('#json-reader').addEventListener('change', async (event)=>{
  console.log(event.path[0].value);
  if (!event.path[0].value.match(/.csv/)) return; // csvかどうか
  let filename = event.target.files[0].name;
  let reader = new FileReader();
  reader.onload = (event)=>{
    csvArray = event.target.result;
    let csvData = csvArray.split('\n');// 1行ごとに分割する
    let jsonArray = csv2json(csvData);
    const blob = new Blob([JSON.stringify(jsonArray, null, 2)], { type: 'application/json' });
    let link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = filename+'.json';
    link.click();
  };
  reader.readAsText(event.target.files[0]);
});

function csv2json(csvArray){
  var jsonArray = [];

  // 1行目から「項目名」の配列を生成する
  var items = csvArray[0].split(',');

  // CSVデータの配列の各行をループ処理する
  // 配列の先頭要素(行)は項目名のため処理対象外
  // 配列の最終要素(行)は空のため処理対象外
  for (var i = 1; i < csvArray.length; i++) {
    var a_line = new Object();
    // カンマで区切られた各データに分割する
    var csvArrayD = csvArray[i].split(',');
    // 各データをループ処理する
    for (var j = 0; j < items.length; j++) {
      // 要素名：items[j]
      // データ：csvArrayD[j]
      a_line[items[j]] = csvArrayD[j];
    }
    jsonArray.push(a_line);
  }
  return jsonArray;
}