function truncate(str, length) {
    if(str.length > length) return str.substr(0, length - 1) + "...";
    return str;
}


console.log(truncate("What I'd like to tell on this topic is:", 20));

console.log(truncate("Hi everyone!", 20));