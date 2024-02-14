function filterRange(arr, min, max) {
    return arr.filter(item => (item >= min && item <= max));
}

let arr = [5, 3, 8, 1];

let filtered = filterRange(arr, 1, 4);

alert( filtered );

alert( arr );