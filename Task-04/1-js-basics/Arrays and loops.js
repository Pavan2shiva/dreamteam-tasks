let numbers = []
for(let i = 1 ; i <= 30 ; i++){
    numbers.push(i);
}

for(let num of numbers){
    if(num % 4 === 0){
        console.log(num);
    }
}