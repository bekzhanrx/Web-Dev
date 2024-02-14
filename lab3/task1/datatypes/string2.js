function checkSpam(str) {
    str = str.toLowerCase();

    if(str.indexOf("viagra") != -1 || str.indexOf("xxx") != -1) return true;
    return false;
}

console.log(checkSpam('buy ViAgRA now'))
console.log(checkSpam('free xxxxx'))
console.log(checkSpam("innocent rabbit"))