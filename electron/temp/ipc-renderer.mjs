// https://garafu.blogspot.com/2020/07/interprocess-communication-electron.html

/**
 * send message to 
 * @param {string} msg message what you want to send to main process (node.js)
 * @param {object}
 * @return {string} message that from 
 */
async function sendmsg(msg, {isWaitResponse, callback} = void 0){
  if(isWaitResponse === void 0 || typeof(isWaitResponse) == 'boolean' && isWaitResponse == false){
    // normal
  }
}
/**
 * @callback callback
 * @param {string} msg message from main process (node.js)
 * @return {void}
 */
