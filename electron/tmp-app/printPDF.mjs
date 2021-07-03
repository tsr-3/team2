
const ipc = require('electron').ipcRenderer

const printPDFBtn = document.querySelectorAll('body > div > button')[0];

ipc.on('wrote-pdf', function (event, path) {
  const message = `Wrote PDF to: ${path}`
  document.querySelectorAll('body > div > div')[0].innerHTML = message;
});