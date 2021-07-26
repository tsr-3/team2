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
      data.attendance.push(...Local.read('attendance-' + data.lecture.id));
      data.attendance.sort((a,b)=>{
        if(a.time < b.time) return -1;
        if(a.time > b.time) return 1;
        return 0;
      });
    }
    Local.write('attendance-' + data.lecture.id, data.attendance);
    maketable(data.attendance, filename);
    drawgraph(data.attendance, filename);
  };
  // reader.onload = (event) => {
  //   const attend = SaveDataFile.parse(event.target.result);
  //   console.log(attend);
  //   if(!attend.attendance){
  //     alert('this file is not contain attendance data');
  //     return;
  //   }
  //   if(!attend.lecture || !attend.lecture.id)
  //     throw new Error('data.lecture.id is not defined');
  //   const lectid = attend.lecture.id;
  //   const data = {};
  //   data.lecture = Local.read(lectid);
  //   data.attendance = Local.read('attendance-' + lectid);
  //   data.students = Local.read('students');
  //   data.professors = Local.read('professors');
  //   if(!data.professors || !data.students || !data.lecture)
  //     console.log('localdata is not exist');
  //   maketable(attend.attendance, filename);
  //   drawgraph(attend.attendance, filename);
  // };
  reader.readAsText(event.target.files[0]);
});
