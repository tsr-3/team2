// https://garafu.blogspot.com/2020/07/interprocess-communication-electron.html

/**
 * send message to main process(node.js)
 * @param {string} msg message what you want to send to main process (node.js).
 * @param {object} properties
 * - isWaitResponse {bool|undefined} - if you don't want to wait response, set this false. default: true
 * - callback {function(response:text) => void | undefined} - if this setted, 
 * @return {string} message that from main process (node.js).
 */
async function sendmsg(msg, properties = void 0){
  // deploy properties
  const {isWaitResponse, callback} = properties;

  // 
  if(isWaitResponse === void 0 || typeof(isWaitResponse) == 'boolean' && isWaitResponse == false){
    // normal
  }
}
