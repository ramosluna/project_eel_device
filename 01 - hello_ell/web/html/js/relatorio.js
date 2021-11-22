
//set a  data de forma automatica ao carregar a pagina
window.onload = function(){
var d = new Date();
var n = d.toLocaleDateString();
//document.getElementById('d1').innerText = n
document.getElementsByClassName("xl1054877")[0].innerHTML = n
document.getElementsByClassName("xl2074877")[0].innerHTML = n
document.getElementsByClassName("xl2084877")[0].innerHTML = n
//document.getElementsByClassName("xl844877")[0].innerHTML = 'ramos'

//eel.relatorio();
js_sleepCorrent();
}

eel.expose(js_passOrNo)
function js_passOrNo(d) {
console.log("js_passOrNo")
    //document.getElementById(d).innerHTML = "alanna";
    document.getElementsByClassName(d)[0].innerHTML="alanna"
  }

//eel.expose(js_sleepCorrent)
function js_sleepCorrent(){
    let text;
    let corrent = prompt("Please enter your sleep mode value", "0,000526026")
    if(corrent == null || corrent == " "){
      text = "valor nao medido"
      document.getElementsByClassName("xl2084877")[4].innerHTML = text;
    }else{
        document.getElementsByClassName("xl2084877")[4].innerHTML = corrent;
    }
}

function relatorio(){
    eel.relatorio()
  }


