var mbl = document.getElementById('month-before-last');
var lm = document.getElementById('last-month');
var am = document.getElementById('actual-month');
var months = [mbl, lm, am];
var op = document.getElementById('open-payment');
var nv = document.getElementById('normal-view');
var form = document.getElementById('client-register-form');

function show (x) {
    var show = document.getElementsByClassName(x)[0];
    show.style.display = 'block';
}

function hide (x) {
    var show = document.getElementsByClassName(x)[0];
    show.style.display = 'none';
}

function openPayment () {
    var hl = [];
    var pay = document.getElementsByTagName('p');
    for (var i = 0; i < pay.length; i++) {
        if (pay[i].className.indexOf('openPay_') == 0) {
            hl.push(pay[i]);
        }
    }
    console.log(hl);
    for (var i = 0; i < hl.length; i++) {
        var bhl = document.getElementById(hl[i].className);
        if (hl[i].innerText == 'Pago : Não' || hl[i].innerText == 'Paid : Não') {
            bhl.style.background = 'rgba(231, 76, 60, 0.5)';
        } else {
            bhl.style.background = 'rgba(46, 204, 113, 0.5)';
        }
    }
}

function normalView () {
    var cont = document.getElementsByClassName('content')[0];
    var row = cont.getElementsByTagName('tr');
    for (var i = 0; i < row.length; i++) {
        if (i % 2 !== 0) {
            row[i].style.background = 'rgba(0, 0, 0, 0.1)';
        } else{
            row[i].style.background = 'none';
        }
    }
}

function valid (evt) {
    var field = document.getElementsByName('preco')[0].value;
    var input = document.getElementsByTagName('input');
    var erro_valid = document.getElementById('erro-valid');
    var erro_valid2 = document.getElementById('erro-valid2');
    for (var i = 0; i < input.length; i++) {
        if (input[i].value == '') {
            evt.preventDefault();
            erro_valid.style.display = '';
            return false;
        }   
    }
    for (var i = 0; i < field.length; i++) {
        if (!(field[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])) {
            evt.preventDefault();
            erro_valid2.style.display = '';
            return false;
        }
    }
}

for (var i = 0; i < months.length; i++) {
    months[i].onmouseover = function () {
        this.addEventListener('mouseover', show(this.id), false);
    }
    months[i].onmouseleave = function () {
        this.addEventListener('mouseleave', hide(this.id), false);
    }
}

op.addEventListener('click', openPayment, false);

nv.addEventListener('click', normalView, false);

form.addEventListener('submit', valid, false);
