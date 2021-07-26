
const {AES256CBC} = require('./AES256CBC.cjs');
const fs = require('fs');

let students_csv = fs.readFileSync('../../data/学生リスト.csv', 'utf-8');
let professors_csv = fs.readFileSync('../../data/教員・担当科目リスト.csv', 'utf-8');

