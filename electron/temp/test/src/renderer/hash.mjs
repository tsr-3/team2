// hash

window.hash = class{
  static async sha256(text){
    if(typeof(text) !== 'string') return null;
    return Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(text)))).map(v=>v.toString(16).padStart(2,'0')).join('');
    // 64 chars
  }
  static async sha384(text){
    if(typeof(text) !== 'string') return null;
    return Array.from(new Uint8Array(await crypto.subtle.digest('SHA-384', new TextEncoder().encode(text)))).map(v=>v.toString(16).padStart(2,'0')).join('');
    // 96 chars
  }
  static async sha512(text){
    if(typeof(text) !== 'string') return null;
    return Array.from(new Uint8Array(await crypto.subtle.digest('SHA-512', new TextEncoder().encode(text)))).map(v=>v.toString(16).padStart(2,'0')).join('');
    // 128 chars
  }
};

