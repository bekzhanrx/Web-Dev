function aclean(arr) {
    let mp = new Map();

    for(let str of arr) {
        let angrm = str.toLowerCase().split('').sort().join('');
        mp.set(angrm, str);
    }

    return Array.from(mp.values());
}

let arr = ["nap", "teachers", "cheaters", "PAN", "ear", "era", "hectares"];

console.log( aclean(arr) );