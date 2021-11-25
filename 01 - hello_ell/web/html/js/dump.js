
eel.expose(js_showAnaliseEprom363);
function js_showAnaliseEprom363(){
    var target = document.getElementById('relatorio')
    target.setAttribute('id','show')
    var ecuSNumb='';
    var ecuHNumb='';

// trata o ECuSerialNumber
    for ( var x = 491; x<503; x++){//0x01Eb
         ecuSNumb +=  document.getElementById(x).innerHTML
    }
    document.getElementById('ECUSerialNumber').value = ecuSNumb;
    document.getElementById("ECUSerialNumberDec").value = ecuSNumb.slice(16,24);
    ecuSNumb='';    
//fim

//trata FCA_SW_Number
for ( var x = 469; x < 480; x++){
    ecuSNumb +=  document.getElementById(x).innerHTML
    }
    document.getElementById('FCA_SW_Number').value = ecuSNumb;
    var fatiar = '';
    var end = 2;
    for(x=0;x<ecuSNumb.length;x+=2){
        fatiar += ecuSNumb.slice(x,end);
        fatiar += ' ';
        end +=2;
    }
    let convert = convertHexToASCII(fatiar)
    document.getElementById("FCA_SW_NumberDec").value = convert

//trata FCA_HW_Number
for ( var x = 480; x < 491; x++){
    ecuHNumb +=  document.getElementById(x).innerHTML
    }
    document.getElementById("FCA_HW_Number").value = ecuHNumb;
    var fatiar1 = '';
    var end1 = 2;
     for(x=0;x<ecuHNumb.length;x+=2){
        fatiar1 += ecuHNumb.slice(x,end1);
        fatiar1 += ' ';
        end1 += 2;
    }
    let convert1 = convertHexToASCII(fatiar1)
    document.getElementById("FCA_HW_NumberDec").value = convert1
}
//}

function convertHexToASCII(hexString){
    let stringOut = '';
    hexString.split(' ').map((i) => {
    tempAsciiCode = parseInt(i, 16);
    stringOut = stringOut + String.fromCharCode(tempAsciiCode);
    });
    return stringOut.slice(0,-1)
}

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


