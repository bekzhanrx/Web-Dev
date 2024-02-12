alert( null || 2 || undefined );
alert( alert(1) || 2 || alert(3) );
alert(1 && null && 2);
alert( alert(1) && alert(2) );
alert( null || 2 && 3 || 4 );
if (age >= 14 && age <= 90){}
if (age < 14 || age > 90){}
// Runs.
// The result of -1 || 0 = -1, truthy
if (-1 || 0) alert( 'first' );

// Doesn't run
// -1 && 0 = 0, falsy
if (-1 && 0) alert( 'second' );

// Executes
// Operator && has a higher precedence than ||
// so -1 && 1 executes first, giving us the chain:
// null || -1 && 1  ->  null || 1  ->  1
if (null || -1 && 1) alert( 'third' );

