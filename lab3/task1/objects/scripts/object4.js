let menu = {
    width: 200,
    height: 300,
    title: "My menu"
}

multipleNumber(menu);

function multipleNumber(obj) {
    for(key in obj) {
        if(typeof obj[key] == "number") {
            obj[key] *= 2;
        }
    }
}