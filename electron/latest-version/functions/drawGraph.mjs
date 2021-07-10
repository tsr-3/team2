/**
 * make graph
 * @param {[{student: string, ratio: number}]} attenddata
 * 学籍番号があっても良いかも
 *
 * @param filename:str
 * @return {undefined}
 */

function drawgraph(attenddata, filename) {

  let raito = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];

  let body = document.querySelector('body');
  let div = document.createElement('div');
  div.id = "canvas";
  let canvas = document.createElement('canvas');
  let W = 1600;
  let H = 400;
  canvas.width = W;
  canvas.height = H;
  let ctx = canvas.getContext('2d');

  // 棒グラフ for loop
  let color = ['red','grean','yello','blue'];
  for (let i = 0; i < attenddata.length; i++){
    ctx.fillStyle = color[Math.floor(Math.random() * color.length)];
    bar = 100 * raito[Math.floor(Math.random() * raito.length)];
    ctx.fillRect(20, 100 + 15 * i, bar, 10);
    ctx.fillText(bar,25,105 + 15 * i,100);
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