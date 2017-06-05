var num1 = '';
var operator = '';
var num2 = '';
var res = 0, flag = 0;

function display(str) {
    document.getElementById('display-text').innerHTML = str;
}

function num(key) {
    if (flag === 1) {
        num1 = '';
        num2 = '';
        operator = '';
        flag = 0;
    }
    if (operator === '') {
        num1 += key;
    }
    else {
        num2 += key;
    }
    display(num1 + " " +  operator + " " + num2);
}

function operate(symbol) {
    if (flag === 1) {
        num1 = "" + res;
        num2 = "";
        
    }
    operator = symbol;
    display(num1 + " " +  operator);
}

function calculate() {
    var x = parseInt(num1);
    var y = parseInt(num2);
    var res = 0;
    if (operator === '+') {
        res = x + y;
    }
    else if (operator === '-') {
        res = x - y;
    }
    else if (operator === '*') {
        res = x * y;
    }
    else {
        if (y === 0) {
            flag = 1;
            display("error, cannot divide by 0");
            return;
        }
        else
            res = x / y;
    }
    display(num1 + " " +  operator + " " + num2 + ' = ' + res);
    flag = 1;
}
