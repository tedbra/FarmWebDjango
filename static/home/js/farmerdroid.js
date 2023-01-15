
var obj = {"nissan": "sentra", "color": "green"};

localStorage.setItem('myStorage', JSON.stringify(obj));

var obj = JSON.parse(localStorage.getItem('myStorage'));

function choose_language(){

}