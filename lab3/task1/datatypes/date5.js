function getLastDayOfMonth(year, month) {
    let date = new Date(year, month + 1, 0);
    return date.getDay();
}


console.log( getLastDayOfMonth(2012, 0) ); 
console.log( getLastDayOfMonth(2012, 1) ); 
console.log( getLastDayOfMonth(2013, 1) ); 