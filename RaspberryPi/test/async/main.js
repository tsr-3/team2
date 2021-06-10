
let res_sum, res_product; // global

async function main(){
  array = new Array(100000);
  array.fill(Math.random());
  res_sum = sum(array);
  res_product = product(array);
  Promise.allSettled([res_sum, res_product])
    .then(console.log(res_sum, res_product));
}

async function sum(arr){
  let sum = 0, val;
  for(val of arr){
    sum += val;
    console.log('sum: ' + sum);
  }
  return sum;
}

async function product(arr){
  let product = 0, val;
  for(val of arr){
    product *= val;
    console.log('product: ' + product);
  }
  return product;
}

main();
