
function js_dSet(){
     eel.dataSet()

}

function loadDump(){
    limpar()
    eel.dumpHtml()

}

function canoe(){
    document.getElementById("bt").innerHTML = "VC CLICKOU !"
    eel.automatico()
}

function limpar(){
    console.log("caled clear")
    for(var i=0; i<4112;i++){
    //document.getElementById(i).style.backgroundColor = 'white' ;
    document.getElementById(i).style.backgroundColor = "lightblue";
    document.getElementById(i).style.color = "black";
    document.getElementById(i).innerHTML= "";
    document.getElementById('path').innerHTML = 'path Dumps:'
    document.getElementById('dSet').innerHTML = 'path DatSet:'
     }
}

eel.expose(js_setPathDump);
function js_setPathDump(paths){
     document.getElementById('path').innerHTML = paths
    }

eel.expose(js_setPathDataSet);
function js_setPathDataSet(paths){
     document.getElementById('dSet').innerHTML = paths
    }

eel.expose(js_imprimirHex);
function js_imprimirHex(address, valoresdados) {
	var inicio = 0;
	var end = 2; 
        for(var x=0;x<16;x++){
           document.getElementById(address).innerHTML = valoresdados.slice(inicio,end);
           address++;
		   inicio +=2;
		   end += 2;
        }
   }

eel.expose(js_imprimirHexSeForDiferente);
function js_imprimirHexSeForDiferente(address, valoresdados){
/*compara com o que já esta na tela e imprime se estiver igual*/

  var inicio = 0;
	var end = 2;
	var getdump = 0;
  var getDaSet = 0;

        for(var x=0;x<16;x++){

          getDaSet = valoresdados.slice(inicio,end);
          getdump = document.getElementById(address).innerText

          console.log("getDump: " + getdump);
          console.log("getDaSet: " + getDaSet);
          //getDaSet= document.getElementById(address).valoresdados.slice(inicio,end);

          if (getdump == getDaSet){
            //document.getElementById(address).innerHTML = "##";
            document.getElementById(address).style.color = '#e6e6e6' //backgroundColor = '#e6e6e6' //'lightgreen'

          }
         else{
            //document.getElementById(address).innerHTML = valoresdados.slice(inicio,end);
            document.getElementById(address).style.backgroundColor = 'red' ; 
          }
          address++;
          inicio +=2;
          end += 2;

        }
}
