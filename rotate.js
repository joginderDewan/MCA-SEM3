let n = 123456;
let r = 2;
let l = (n+"").length; //length of the string 
let div = Math.pow(10,2);
let mult = Math.pow(10,l-r);
let q = Math.floor(n/div);
let rem  = n % div;
let rn = q + rem*mult;
console.log(rn)