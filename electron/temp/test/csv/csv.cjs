// csv enc/dec //

exports.CSV = class{
  static parse(string){
    let separated = string.split(/(?<!")"(?!")/), data = [], object = [], rows = [], isJoin = false;
    // data separated
    separated.forEach((value, index)=>{
      if(!value) return;
      if(index % 2){
        // odd => in ""
        data.push(0xb, (value.replace(/"""/g, '"')).replace(/\r\n/g, '\r\n'));
      } else{
        // even => out of ""
        for(let line of value.split(/\r\n|\n/g))
          data.push(...((line.replace(/"""/g, '"')).split(/,/g)), 0xd);
      }
    });
    for(let val of data){
      if(!val) continue;
      if(val === 0xb){
        // join
        isJoin = true;
        continue;
      }
      if(isJoin){
        let prev = rows.pop();
        if(prev === void 0) prev = '';
        rows.push(prev + val);
        isJoin = false;
        continue;
      }
      if(val === 0xd){
        // return
        object.push(rows);
        rows = [];
        continue;
      }
      rows.push(val);
    }
    object.push(rows);
    return object;
  };
  static stringify(value, direction = 'row'){
    if(!direction.match(/^(row|column)$/)) throw new Error('direction needs "row" or "column"');
    if(typeof(value) != 'object'){
      // not object
      if(typeof(value) == 'function') value = '[function]' + value.name;
      return '' + value;
    }
    let dat = [];
    if(Array.isArray(value)){
      // array
      let isarr = true;
      for(let val of value)
        if(!Array.isArray(val)){
          isarr = false;
          break;
        }
      if(isarr){
        //  over 2 demention array
        for(let temp of value){
          let line = [];
          for(let val of temp){
            line.push(this.stringify(val, direction).replace(/"/g, '"""'));
          }
          dat.push(line)
        }
      }
    } else{
      // object
    }
    // to string
    let string = '';
    if(direction == 'row'){
      // row
      for(let temp in dat){
        for(let val in dat)
          if(val.match(/\n|,/)) string += '"' + val + '"';
          else string += val;
      }
    } else{
      // column
    }
  }
};