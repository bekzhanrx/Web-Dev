let salaries = {
    John: 100,
    Ann: 160,
    Peter: 130
}

let sum = 0;

for(key in salaries) {
    sum += salaries[key];
}

alert(sum);