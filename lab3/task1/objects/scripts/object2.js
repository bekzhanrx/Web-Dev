let scheudle = {};

alert(isEmpty(scheudle));

scheudle["8:30"] = "get up";

alert(isEmpty(scheudle));

function isEmpty(obj) {
    for(key in obj) {
        return false;
    }
    return true;
}