// csv enc/dec //

exports.CSV = class{
  static parse(string){
    let separated = string.split(/(?<!")"(?!")/), data = [], object = [], rows = [], isJoin = false;
    // data separated
    separated.forEach((value, index)=>{
      if(!value) return;
      if(index % 2){
        // odd => out of ""
        data.push(0xb, (value.replace(/"""/g, '"')).replace(/\r\n/g, '\r\n'));
      } else{
        // even => in ""
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
  }
};
