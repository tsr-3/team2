
/**
 * save to localdata
 * @param {string} lecture 
 * @param {object} data 
 */
export function save(lecture, data){
  Electron.ipcRenderer.sendSync('load-localdata', {lect: lecture, odr: data});
}

/**
 * load from localdata
 * @param lecture 
 */
export function load(lecture){
  //
}
