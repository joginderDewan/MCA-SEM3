let n = 20;
for(let i = 1;i<=20;i++){
    let flag = true;
    for(let j=2;j<i;j++){
        if(i%j==0){
            flag = false;
            break;
        }
    }
    if(flag){
        console.log(i,"Is prime");
    }else{
        console.log(i,"Is not prime");
    }
}
