window.calc_add = async function(first, second){
  return Electron.ipcRenderer.sendSync('calc_add', {message: [first, second]});
}