let attend = {}
let t2pecf = {}

import * as SaveDataFile from './SaveDataFile.mjs';
import * as Local from './SaveLocalData.mjs';

// from: https://zukucode.com/2017/04/javascript-date-format.html
function formatDate (date, format) {
  format = format.replace(/yyyy/g, date.getFullYear());
  format = format.replace(/MM/g, ('0' + (date.getMonth() + 1)).slice(-2));
  format = format.replace(/dd/g, ('0' + date.getDate()).slice(-2));
  format = format.replace(/HH/g, ('0' + date.getHours()).slice(-2));
  format = format.replace(/mm/g, ('0' + date.getMinutes()).slice(-2));
  format = format.replace(/ss/g, ('0' + date.getSeconds()).slice(-2));
  format = format.replace(/SSS/g, ('00' + date.getMilliseconds()).slice(-3));
  return format;
};


document.querySelector('form.file-reader > input#student-reader').addEventListener('change', async (event) => {
  if (!event.path[0].value.match(/.json$|.t2pecf$/)) {
    document.querySelector('#filetype-check').innerText = 'invalid filetype "' + event.path[0].value.match(/\..+$/)[0] + '"';
    document.querySelector('#filetype-check').classList.add('error')
  }
  let reader = new FileReader();
  const filename = event.path[0].value.match(/[^\/\\]+\.[^\/\\]+$/g)[0];
  reader.onload = event=>{
    const data = SaveDataFile.parse(event.target.result);
    if(!data.attendance || !data.lecture || !data.lecture.id){
      alert('this file is not contain attendance data or lecture id');
      return;
    }
    if(Object.keys(data.lecture).length < 2)
    data.lecture = Local.read(data.lecture.id);
    if(!data.students)
    data.students = Local.read('students');
    if(!data.professors)
    data.professors = Local.read('professors');
    if(Local.exist('attendance-' + data.lecture.id)){
      // marge attendance data
      let localdat = Local.read('attendance-' + data.lecture.id);
      let localstart = (()=>{
        let startlist = [];
        for(const val of localdat)
          if(val.student == 'start') startlist.push(val.time);
        return startlist;
      })();
      let datastart = (()=>{
        for(const val of data.attendance)
          if(val.student == 'start') return val;
        alert('this file is not contain attendance data or lecture id');
        return void 0;
      })();
      if(datastart === void 0) return;
      let temp = data.attendance;
      data.attendance = localdat;
      if(localstart.indexOf(datastart.time.toISOString()) < 0)
        data.attendance.push(...temp);
      data.attendance.sort((a,b)=>{
        if(a.time < b.time) return -1;
        if(a.time > b.time) return 1;
        return 0;
      });
    }
    Local.write('attendance-' + data.lecture.id, data.attendance);
    // remove start
    {
      let cnt = 0;
      while(true){
        if(cnt > data.attendance.length - 1) break;
        if(data.attendance[cnt].student != 'start') cnt++;
        else
          data.attendance.splice(cnt, 1);
      }
    }
    // judge attend/late/abcent
    {
      const time = {};
      time.start = data.lecture.start;
      time.late = data.lecture.late;
      time.limit = data.lecture.limit;
      console.log(data);
      for(const index in data.attendance){
        let accept = data.attendance[index].time;
        if(accept instanceof Date) accept = accept.toISOString();
        let temptime = new Date(accept.split('T')[0] + time.start);
        // set beforelate
        temptime.setMinutes(temptime.getMinutes() + time.late);
        if(accept < temptime){
          data.attendance[index].attend = '出席';
          continue;
        }
        temptime.setMinutes(temptime.getMinutes() + time.limit);
        if(accept < temptime){
          data.attendance[index].attend = '遅刻';
          continue;
        }
        data.attendance[index].attend = '欠席';
      }
    }
    // create time str
    for(const index in data.attendance){
      let time = data.attendance[index].time;
      if(!(time instanceof Date)) time = new Date(time);
      data.attendance[index].time = formatDate(time, 'yyyy/MM/dd HH:mm:ss');
    }
    // count times of attendances
    const attendCountObj = {};
    const attendCount = [];
    for(const index in data.attendance){
      const value = data.attendance[index];
      value.name = (()=>{
        if(value.student == void 0) return;
        for(const val of data.students){
          if(val.id == value.student) return val.name;
        }
        return void 0;
      })();
      if(!attendCountObj[value.student]) attendCountObj[value.student] = 1;
      else attendCountObj[value.student]++;
    }
    for(const key of Object.keys(attendCountObj))
      attendCount.push({
        student: (()=>{
          for(const val of data.students){
            if(val.id == key) return val.name;
          }
          return void 0;
        })(),
        count: attendCountObj[key]
      });
    // draw
    maketable(data.attendance, filename);
    drawgraph(attendCount, filename);
  };
  reader.readAsText(event.target.files[0]);
});
