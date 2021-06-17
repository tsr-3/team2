// renderer process

async function send(first, second){
  electron.ipcRenderer.sendSync('calc_add', {message: [first, second]});
}
