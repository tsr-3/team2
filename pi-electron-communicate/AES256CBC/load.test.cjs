
const {AES256CBC} = require('./AES256CBC.cjs');
const fs = require('fs');

(async ()=>{
  let cipher = fs.readFileSync('../../RaspberryPi/functions/test/t2pecf/sdf-test.dat', 'utf-8');

  let data = {};
  data.type = cipher.substr(0, 8);
  data.data = cipher.substr(8).split(/\./g);
  for(let index in data.data){
    let object = {};
    const string = data.data[index];
    object.type = string.substr(0, 7);
    object.key = string.substr(7, 43) + '=';
    object.iv = string.substr(7 + 43, 22) + '==';
    object.data = string.substr(7 + 43 + 22);
    data.data[index] = object;
  }
  for(let dat of data.data)
    data[dat.type] = await AES256CBC.decode(dat.key, dat.iv, dat.data);
  
  delete data.data;
  delete data.type;

  fs.writeFileSync('load.test.out.json', JSON.stringify(data));
})();
