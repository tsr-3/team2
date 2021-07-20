
function parse(string){
  const dat = JSON.parse(string);
  if(dat.attendance){
    dat.attendance = dat.attendance.split(/\r\n|\n/g);
    for(const index in dat.attendance){
      const value = dat.attendance[index];
      let [date, time, id] = value.split(/ /g);
      dat.attendance[index] = {};
      dat.attendance[index].student = id;
      dat.attendance[index].time = new Date(date + 'T' + time + '+0900');
    }
  }
  return dat;
}

function stringify(object){
  const _attendance = object.attendance;
  if(object.attendance){
    object.attendance = new Array(_attendance.length);
    for(const index in _attendance){
      const {student, time} = _attendance[index];
      object.attendance[index] = time.toISOString().replace(/T/, ' ').replace(/\.[0-9]+Z/, '') + ' ' + student;
    }
  }
  const json = JSON.stringify(object);
  object.attendance = _attendance;
  return json;
}
