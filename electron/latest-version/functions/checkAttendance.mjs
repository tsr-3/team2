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
  reader.onload = (event) => {
    const attend = SaveDataFile.parse(event.target.result);
    if(!attend.lecture || !attend.lecture.id)
      throw new Error('data.lecture.id is not defined');
    const lectid = attend.lecture.id;
    const data = {};
    data.lecture = Local.read(lectid);
    data.students = Local.read('students');
    data.professors = Local.read('professors');
    if(!data.professors || !data.students || !data.lecture)
      console.log('localdata is not exist');
    maketable(attend.attendance, filename);
    drawgraph(attend.attendance, filename);
  };
  reader.readAsText(event.target.files[0]);
});
