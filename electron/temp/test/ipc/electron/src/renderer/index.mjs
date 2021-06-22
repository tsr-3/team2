async function calc_add(first, second){
  Electron.ipcRenderer.sendSync('calc_add', {message: [first, second]});
}