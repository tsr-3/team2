let attend = {}
let t2pecf = {}

document.querySelector('form.file-reader > input#student-reader').addEventListener('change', async (event) => {
  if (!event.path[0].value.match(/.json$|.t2pecf$/)) {
    document.querySelector('#filetype-check').innerText = 'invalid filetype "' + event.path[0].value.match(/\..+$/)[0] + '"';
    document.querySelector('#filetype-check').classList.add('error')
  }
  let reader = new FileReader();
  reader.onload = (event) => {
    test = event.target.result.value;
    console.log(test)

    maketable(attend.attendance, filename);
    drawgraph(attend.attendance, filename);
    console.log(attend)
  };
  console.log(attend)
  console.log('とぅるー');
})
