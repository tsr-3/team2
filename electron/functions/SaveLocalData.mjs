
// /**
//  * save to localdata
//  * @param {string} lecture
//  * @param {object} data
//  */
// export function save(lecture, data){
//   Electron.ipcRenderer.sendSync('post-localdata', {lect: lecture, odr: data});
// }

// /**
//  * load from localdata
//  * @param lecture
//  */
// export function load(lecture, data){
//   Electron.ipcRenderer.sendSync('get-localdata', {lect: lecture, odr:data});
// }

// /**
//  * send request to localdata
//  * @param {'GET' | 'PUT' | 'DELETE'} method
//  * @param {[string]} path ['lecture-id', 'keyname', 'keyname', ...]
//  * @param {any} data put/post: data you want to set
//  * @return {object} result: exit status code, data: return data
//  */
// export function send(method, path, data = void 0){
//   return Electron.ipcRenderer.sendSync('req-localdata', {method: method, path: path, data: data});
// }

export function write(filename, data){
  return Electron.ipcRenderer.sendSync('write-local', {filename, data});
}
export function read(filename){
  return Electron.ipcRenderer.sendSync('read-local', filename);
}
export function unlink(filename){
  return Electron.ipcRenderer.sendSync('delete-local', filename);
}
export function exist(filename) {
  return Electron.ipcRenderer.sendSync('exist-local', filename);
}

