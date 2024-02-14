function unique(arr) {
    let ans = [];
    for(let str of arr) {
        if(!ans.includes(str)) {
            ans.push(str);
        }
    }
    return ans;
}

let strings = ["Hare", "Krishna", "Hare", "Krishna",
  "Krishna", "Krishna", "Hare", "Hare", ":-O"
];

console.log( unique(strings) );