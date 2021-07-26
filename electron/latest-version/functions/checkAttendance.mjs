let attend = {}
let t2pecf = {}

import * as SaveDataFile from './SaveDataFile.mjs';
import * as Local from './SaveLocalData.mjs';

document.querySelector('form.file-reader > input#student-reader').addEventListener('change', async (event) => {
  if (!event.path[0].value.match(/.json$|.t2pecf$/)) {
    document.querySelector('#filetype-check').innerText = 'invalid filetype "' + event.path[0].value.match(/\..+$/)[0] + '"';
    document.querySelector('#filetype-check').classList.add('error')
  }
  let reader = new FileReader();
  console.log(event.path[0].value)
  const filename = event.path[0].value.match(/[^\/\\]+\.[^\/\\]+$/g)[0];
  reader.onload = event=>{
    const data = SaveDataFile.parse(event.target.result);
    console.log(data);
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
        for(const val of localdat)
          if(val.student == 'start') return val;
        alert('this file is not contain attendance data or lecture id');
        return void 0;
      })();
      if(localstart == void 0) return void 0;
      data.attendance.push(localdat);
      data.attendance.sort((a,b)=>{
        if(a.time < b.time) return -1;
        if(a.time > b.time) return 1;
        return 0;
      });
    }
    Local.write('attendance-' + data.lecture.id, data.attendance);
    // marge list
    const attendCountObj = {};
    const attendCount = [];
    for(const index in data.attendance){
      const value = data.attendance[index];
      value.name = (()=>{
        for(const val in data.students)
          if(val.id == value.student) return val.name;
        return void 0;
      })();
      if(!attendCountObj[value.student]) attendCountObj[value.student] = 1;
      else attendCountObj[value.student]++;
    }
    for(const key of Object.keys(attendCountObj))
      attendCount.push({student: key, count: attendCountObj[key]});
    console.log(attendCount, data);
    // draw
    maketable(data.attendance, filename);
    drawgraph(attendCount, filename);
  };
  reader.readAsText(event.target.files[0]);
});
