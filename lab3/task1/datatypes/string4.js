function extractCurrencyValue(money) {
    return +money.slice(1);
}


console.log(extractCurrencyValue('$120'));