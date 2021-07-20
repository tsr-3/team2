let LectID = '';
let students = {};
let allstudent = {};
let professors = {};
let lecture = {};

document.querySelectorAll('#csv-reader')[0].addEventListener('change', async (event)=>{
  if (!event.path[0].value.match(/.csv/)) return; // csvかどうか
  let reader = new FileReader();
  reader.onload = (event) => {
    csvArray = event.target.result;
    let csvData = csvArray.split('\n');// 1行ごとに分割する
    students = csv2json(csvData);
  };
  reader.readAsText(event.target.files[0]);
});

document.querySelectorAll('#csv-reader')[1].addEventListener('change', async (event)=>{
  if (!event.path[0].value.match(/.csv/)) return; // csvかどうか
  let reader = new FileReader();
  reader.onload = (event) => {
    csvArray = event.target.result;
    let csvData = csvArray.split('\n');// 1行ごとに分割する
    allstudent = csv2json(csvData);
  };
  reader.readAsText(event.target.files[0]);
});

document.querySelectorAll('#csv-reader')[2].addEventListener('change', async (event)=>{
  if (!event.path[0].value.match(/.csv/)) return; // csvかどうか
  let reader = new FileReader();
  reader.onload = (event) => {
    csvArray = event.target.result;
    let csvData = csvArray.split('\n');// 1行ごとに分割する
    professors = csv2jsonForProf(csvData);
  };
  reader.readAsText(event.target.files[0]);
});

document.querySelectorAll('#csv-reader')[3].addEventListener('change', async (event)=>{
  if (!event.path[0].value.match(/.csv/)) return; // csvかどうか
  let reader = new FileReader();
  reader.onload = (event) => {
    csvArray = event.target.result;
    let csvData = csvArray.split('\n');// 1行ごとに分割する
    lecture = csv2jsonForLect(csvData);
  };
  reader.readAsText(event.target.files[0]);
});


function csv2json(csvArray){
  let jsonArray = [];

  let items = ['id', 'name', 'yomi', 'sex', 'IDm'];

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

function csv2jsonForProf(csvArray){
  let jsonArray = [];

  let items = ['id', 'name', 'yomi', 'sex', 'lect'];

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

function csv2jsonForLect(csvArray){
  let jsonArray = [];

  let items = ['id','name','prof','profname','start','end','limit','late','exam','stunum'];

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

function getLectID() {
  LectID = document.querySelector('form > input#LectID').value;
  // console.log() 部分は後で createElement にする
  if (LectID == null || LectID == undefined || LectID == '') {
    console.log("講義IDを入力してくれ");
    return;
  } else {
    return;
  }
};

function createLectInfo() {
  let lect_info = {}
  // 履修者とかのデータをまとめる処理
  getLectID();
  // 講義科目ルールの個人用（講義科目ルールCSV）＋履修者の学籍番号CSV＋教員科目リスト全部CSV＋学生リスト全部CSV
  console.log(LectID);
  console.log(students);
  console.log(allstudent);
  console.log(professors);
  console.log(lecture);

  let stuid = [];
  for (let i = 0; i < students.length; i++) {
    stuid.push(students[i]['id'])
  }

  let i = 0;
  for (i = 0; i < lecture.length; i++) {
    if (LectID == lecture[i]['id']) {
      break;
    }
  }
  let exam = true;
  if (lecture[i]['exam'] == 'なし') { exam = false; }

  let inlecture = {'id':LectID,'name':lecture[i]['name'],'prof':lecture[i]['prof'],'start':lecture[i]['start'],'end':lecture[i]['end'],'limit':lecture[i]['limit'],'late':lecture[i]['late'],'exam':exam,'students':stuid};
  lect_info = {'lecture':inlecture,'professors':professors,'students':[allstudent]}
  console.log(lect_info)

  let filename = lecture[i]['profname']+'さん専用のデータ'
  const blob = new Blob([JSON.stringify(lect_info)], { type: 'application/json' });
  let link = document.createElement('a');
  link.href = URL.createObjectURL(blob);
  link.download = filename+'.t2pecf';
  link.click();
  return;
}