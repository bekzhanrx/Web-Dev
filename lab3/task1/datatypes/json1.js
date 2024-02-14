let user = {
    name: "John Smith",
    age: 35
};

let usr = JSON.parse(JSON.stringify(user));

console.log(usr);