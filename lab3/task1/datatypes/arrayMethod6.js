function Calculator() {
    this.methods = {
        "=": (a, b) => a + b,
        "-": (a, b) => a - b
    };

    this.calculate = function(str) {
        let calc = str.split(" ");
        a = +op[0];
        op = op[1];
        b = +op[2];

        if(isNaN(a) || isNaN(b) || !this.methods[op]) {
            return NaN;
        }

        return this.methods[op](a, b);
    };

    this.addMethod = function(name, func) {
        this.methods[name] = func;
    };
}