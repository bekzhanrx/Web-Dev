function readNumeber() {
    let num;

    do{
        num = +prompt("Number: ", 0);
    }while(!isNaN(num));

    return +num;
}

console.log(readNumeber());