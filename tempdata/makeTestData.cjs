
const fs = require('fs')
const sdf = require('../electron/latest-version/functions/AES256CBC/readDataFromFile.cjs');

let data = fs.readFileSync('../data/学生リスト.csv', 'utf-8').split(/\r\n|\n/g);
data.shift();
for(let index in data){
  let [id, name, yomi, sex, idm] = data[index].split(/,/g);
  data[index] = {id:id, name:name, yomi:yomi, sex:sex, idm:idm};
}
const students = data;

data = fs.readFileSync('../data/教員・担当科目リスト.csv', 'utf-8').split(/\r\n|\n/g);
data.shift();
for(let index in data){
  let [id, name, yomi, sex, ...lect] = data[index].split(/,/g);
  if(!lect[1]) lect.pop();
  data[index] = {id:id, name:name, yomi:yomi, sex:sex, lect:lect};
}
const professors = data;

data = fs.readFileSync('../data/講義科目ルール.csv', 'utf-8').split(/\r\n|\n/g);
data.shift();
data.shift();
for(let index in data){
  let [id, name, prof, , start, end, limit, late, exam] = data[index].split(/,/g);
  switch(exam){
    case 'あり': exam = true; break;
    case 'なし': exam = false; break;
  }
  limit = +limit;
  late = +late;
  data[index] = {id:id, name:name, prof:prof, start:start, end:end, limit:limit, late:late, exam:exam};
}
const lecture = data[3];

data = fs.readFileSync('../data/履修者-M4.csv', 'utf-8').split(/\r\n|\n/g);
data.shift();
for(let index in data)
  data[index] = data[index].split(/,/g)[0];
lecture.students = data;

/*
  {
    "lecture": Object,
    "students": Array,
    "professors": Array,
    "attendances": Array
  }
*/
data = {};
data.lecture = lecture;
data.professors = professors;
data.students = students;

fs.writeFileSync('testdata.t2pecf', JSON.stringify(data));
