/**
 * make graph
 * 名前と(学籍番号と)出席回数
 * @param {[{student: string, count: number}]} attenddata
 * 学籍番号があっても良いかも
 *
 * @param filename:str
 * @return {undefined}
 */

function drawgraph(attenddata, filename) {

  let raito = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]; /* テストデータ */

  let body = document.querySelector('body');
  let div = document.createElement('div');
  div.id = "canvas";
  let canvas = document.createElement('canvas');
  let W = 600;
  let H = 20*attenddata.length+40;
  canvas.width = W;
  canvas.height = H;
  let ctx = canvas.getContext('2d');

  // 棒グラフ for loop
  for (let i = 0; i < attenddata.length; i++){
    ctx.fillStyle = 'black';
    let count = raito[Math.floor(Math.random() * raito.length)];//出席回数
    //let count = attenddata[i]['raito']
    let bar = count * W / raito.length;
    let barheight = 20 + 20 * i;
    ctx.fillRect(20, barheight, bar, 10);
    ctx.fillStyle = 'black';
    let datatext = '名前：' + attenddata[i]['name'] + ' 出席回数：' + count;
    ctx.fillText(datatext,25,barheight-1.5);
  }

  // x軸の描画
  ctx.beginPath();
  ctx.moveTo(10, H-20);
  ctx.lineTo(W-10, H-20);
  ctx.closePath();
  ctx.stroke();

  // y軸の描画
  ctx.beginPath();
  ctx.moveTo(20, H-10);
  ctx.lineTo(20, 10);
  ctx.closePath();
  ctx.stroke();

  div.appendChild(canvas)
  body.appendChild(div)
}