let attend = {}
let t2pecf = {}

import * as SaveDataFile from './SaveDataFile.mjs';

document.querySelector('form.file-reader > input#student-reader').addEventListener('change', async (event) => {
  if (!event.path[0].value.match(/.json$|.t2pecf$/)) {
    document.querySelector('#filetype-check').innerText = 'invalid filetype "' + event.path[0].value.match(/\..+$/)[0] + '"';
    document.querySelector('#filetype-check').classList.add('error')
  }
  let reader = new FileReader();
  const filename = event.target.files[0];
  reader.onload = (event) => {
    const attend = SaveDataFile.parse(event.target.result);
    console.log(attend);

    maketable(attend.attendance, filename);
    drawgraph(attend.attendance, filename);
  };
  reader.readAsText(filename);
})
