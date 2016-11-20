var mbl = document.getElementById('month-before-last');
var lm = document.getElementById('last-month');
var am = document.getElementById('actual-month');
var op = document.getElementById('open-payment');
var nv = document.getElementById('normal-view');
var months = [mbl, lm, am];

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
    for (var i = 0; i < hl.length; i++) {
        var bhl = document.getElementById(hl[i].className);
        if (hl[i].textContent == 'Pago: Não') {
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
