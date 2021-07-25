
console.log('load ipc-mainprocess');

const LocalPath = __dirname.replace(/functions(|\/)$/,'.appdata/'); // team2/electron/latest-version/.appdata/

const electron = require('electron');
const fs = require('fs');
// const {AES256CBC} = require('./AES256CBC/AES256CBC.js');

// electron.ipcMain.on('req-localdata', (event, {method, path, data})=>{
//   console.log(method, path, data);
//   event.returnValue = (()=>{
//     // check is  localdata dir exist
//     if(!fs.existsSync(LocalPath))
//       fs.mkdirSync(LocalPath);
//     // check is file exist
//     const FilePath = LocalPath + path.shift() + '.t2ld';
//     if(!fs.existsSync(FilePath)){
//       if(method.toLowerCase() == 'put')
//         fs.writeFileSync(FilePath, ''); // make new file
//       else if(method.toLowerCase() == 'delete')
//         return {result: 'not_exist'}; // たぶんtrueでいいけど、pathが間違ってた時にtrueだと気づけなさそう
//       else return {result: false};
//     }
//     // load file
//     let filedata = fs.readFileSync(FilePath, 'utf-8');
//     if(!filedata) filedata = '{}'; 
//     const dataobject = JSON.parse(filedata);
//     // switch method
//     switch(method.toLowerCase()){
//       case 'get':
//         try{
//           return Function('_',`return _['${path.join(`']['`)}']`)(dataobject);
//         } catch{
//           return void 0;
//         }
//       case 'put':
//         {
//           try{
//             // try to access
//             Function('_',`return _['${path.join(`']['`)}']`)(dataobject);
//           } catch{
//             // make that path
//             const f = (path, object)=>{
//               if(path.length < 1) return;
//               if(path.length == 1){
//                 object[path[0]] = void 0;
//                 return void 0;
//               }
//               const key = path.shift();
//               if(object[key] === void 0) object[key] = {};
//               f(path, object[key]);
//             };
//           }
//           const origin = Function('_',`return _['${path.join(`']['`)}']`)(dataobject);
//           Function('_', '_d',`return _['${path.join(`']['`)}']=_d`)(dataobject, data);
//           fs.writeFileSync(FilePath, JSON.stringify(dataobject));
//           return origin;
//         }
//       case 'delete':
//         {
//           try{
//             // try to access
//             Function('_',`return _['${path.join(`']['`)}']`)(dataobject);
//           } catch{
//             return {result: 'not_exist'};
//           }
//           const origin = Function('_',`return _['${path.join(`']['`)}']`)(dataobject);
//           Function('_',`return _['${path.join(`']['`)}']`)(dataobject);
//           fs.writeFileSync(FilePath, JSON.stringify(dataobject));
//           return origin;
//         }
//       default:
//         return {result:false};
//     }
//   })();
// });

electron.ipcMain.on('write-local', (event, {filename, data})=>{
  event.returnValue = (()=>{
    const FilePath = LocalPath + filename + '.t2ld';
    let response;
    if(fs.existsSync(FilePath)) response = fs.readFileSync(FilePath, {encoding: 'utf-8'});
    else response = true;
    fs.writeFileSync(FilePath, JSON.stringify(data));
    return response;
  })();
});
electron.ipcMain.on('read-local', (event, filename)=>{
  event.returnValue = (()=>{
    const FilePath = LocalPath + filename + '.t2ld';
    if(!fs.existsSync(FilePath)) return false;
    return JSON.parse(fs.readFileSync(FilePath, {encoding: 'utf-8'}));
  })();
});
electron.ipcMain.on('delete-local', (event, filename)=>{
  event.returnValue = (()=>{
    const FilePath = LocalPath + filename + '.t2ld';
    if(!fs.existsSync(FilePath)) return true;
    let response =  JSON.parse(fs.readFileSync(FilePath, {encoding: 'utf-8'}));
    fs.unlinkSync(FilePath);
    return response;
  })();
});
