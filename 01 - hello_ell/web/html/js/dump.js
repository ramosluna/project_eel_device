//#region js_showAnaliseEprom363
eel.expose(js_showAnaliseEprom363);
function js_showAnaliseEprom363(){
    var target = document.getElementById('relatorio')
    target.setAttribute('id','show')
    var getHexPlanilha='';

// trata o ECuSerialNumber
    for ( var x = 491; x<503; x++){//0x01Eb
         getHexPlanilha +=  document.getElementById(x).innerHTML
    }
    document.getElementById('ECUSerialNumber').value = getHexPlanilha;
    document.getElementById("ECUSerialNumberDec").value = getHexPlanilha.slice(16,24);
    getHexPlanilha='';
//fim

//trata FCA_SW_Number
for ( var x = 469; x < 480; x++){
    getHexPlanilha +=  document.getElementById(x).innerHTML
    }
    document.getElementById('FCA_SW_Number').value = getHexPlanilha;
    var fatiar = '';
    var end = 2;
    for(x=0;x<getHexPlanilha.length;x+=2){
        fatiar += getHexPlanilha.slice(x,end);
        fatiar += ' ';
        end +=2;
    }
    let convert = convertHexToASCII(fatiar)
    document.getElementById("FCA_SW_NumberDec").value = convert
    getHexPlanilha='';

//trata FCA_HW_Number
for ( var x = 480; x < 491; x++){
    getHexPlanilha +=  document.getElementById(x).innerHTML
    }
    document.getElementById("FCA_HW_Number").value = getHexPlanilha;
    var fatiar1 = '';
    var end1 = 2;
     for(x=0;x<getHexPlanilha.length;x+=2){
        fatiar1 += getHexPlanilha.slice(x,end1);
        fatiar1 += ' ';
        end1 += 2;
    }
    let convert1 = convertHexToASCII(fatiar1)
    document.getElementById("FCA_HW_NumberDec").value = convert1
    getHexPlanilha='';

    //EcuIdentFiatSparePartNo (0x0195)
    for ( var x = 405; x < 416; x++){
        getHexPlanilha +=  document.getElementById(x).innerHTML
        }
        document.getElementById("EcuIdentFiatSparePartNo_number").value = getHexPlanilha;
        var fatiar2 = '';
        var end2 = 2;
         for(x=0;x<getHexPlanilha.length;x+=2){
            fatiar2 += getHexPlanilha.slice(x,end2);
            fatiar2 += ' ';
            end2 += 2;
        }
        let convert2 = convertHexToASCII(fatiar2)
        document.getElementById("EcuIdentFiatSparePartNo_Dec").value = convert2
        getHexPlanilha='';

  //  EcuIdentEcuHWNo (0x01B1)
      for ( var x = 433; x < 444; x++){
        getHexPlanilha +=  document.getElementById(x).innerHTML
        }
        document.getElementById("EcuIdentEcuHWNo_number").value = getHexPlanilha;
        var fatiar3 = '';
        var end3 = 2;
         for(x=0;x<getHexPlanilha.length;x+=2){
            fatiar3 += getHexPlanilha.slice(x,end3);
            fatiar3 += ' ';
            end3 += 2;
        }
        let convert3 = convertHexToASCII(fatiar3)
        document.getElementById("EcuIdentEcuHWNo_Dec").value = convert3
        getHexPlanilha='';

  //ApplDataFingerprint (0x0188):
  for ( var x = 392; x < 405; x++){
        getHexPlanilha +=  document.getElementById(x).innerHTML
        }
        let gDFHex = document.getElementById("ApplDataFingerprint_number").value = getHexPlanilha;

        document.getElementById("ApplDataFingerprint_Dec").value = gDFHex.slice(20,26);
        document.getElementById("ApplDataFingerprint_Dec").style.color = "red"

        getHexPlanilha='';

   //ApplSWFingerprint (0x017B):
  for ( var x = 379; x < 392; x++){
        getHexPlanilha +=  document.getElementById(x).innerHTML
        }
        let gSWHex = document.getElementById("ApplSWFingerprint_number").value = getHexPlanilha;

        document.getElementById("ApplSWFingerprint_Dec").value = gSWHex.slice(20,26);
        document.getElementById("ApplSWFingerprint_Dec").style.color = "red"

        getHexPlanilha='';

  //BootSWFingerprint (0x016E)
  for ( var x = 366; x < 379; x++){
        getHexPlanilha +=  document.getElementById(x).innerHTML
        }
        let gBSWHex = document.getElementById("BootSWFingerprint_number").value = getHexPlanilha;

        document.getElementById("BootSWFingerprint_Dec").value = gBSWHex.slice(20,26);
        document.getElementById("BootSWFingerprint_Dec").style.color = "red"

        getHexPlanilha='';

  //Dataset SET (10A0) DataSet_number 8
  var getHexData = '';
  var getHexIndex = '';
        for ( var x = 4256; x < 4264; x++){
            getHexData +=  document.getElementById(x).innerHTML
        }
        for ( var x = 4264; x < 4266; x++){
            getHexIndex +=  document.getElementById(x).innerHTML
        }
        document.getElementById("DataSet_number").value = getHexData;
        document.getElementById("DataSet_index_number").value = getHexIndex;

        var fatiar3 = '';
        var end3 = 2;
         for(x=0;x<getHexData.length;x+=2){
            fatiar3 += getHexData.slice(x,end3);
            fatiar3 += ' ';
            end3 += 2;
        }     
        let convert4 = convertHexToASCII(fatiar3)
        document.getElementById("DataSet_Asci_number").value = convert4

        var fatiar3 = '';
        var end3 = 2;
         for(x=0;x<getHexIndex.length;x+=2){
            fatiar3 += getHexIndex.slice(x,end3);
            fatiar3 += ' ';
            end3 += 2;
        }
        let convert5 = convertHexToASCII(fatiar3)
        document.getElementById("DataSet_Asci_index").value = convert5

//Dataset KDS (0x164)

    var getKdsData = '';
    var getKDSIndex = '';
        for ( var x = 356; x < 364; x++){
            getKdsData +=  document.getElementById(x).innerHTML
        }
        for ( var x = 364; x < 366; x++){
            getKDSIndex +=  document.getElementById(x).innerHTML
        }
        document.getElementById("kds_number").value = getKdsData;
        document.getElementById("kds_index").value = getKDSIndex;

        var fatiar3 = '';
        var end3 = 2;
         for(x=0;x<getKdsData.length;x+=2){
            fatiar3 += getKdsData.slice(x,end3);
            fatiar3 += ' ';
            end3 += 2;
        }     
        let convert6 = convertHexToASCII(fatiar3)
        document.getElementById("kds_asci_number").value = convert6

        var fatiar3 = '';
        var end3 = 2;
         for(x=0;x<getKDSIndex.length;x+=2){
            fatiar3 += getKDSIndex.slice(x,end3);
            fatiar3 += ' ';
            end3 += 2;
        }
        let convert7 = convertHexToASCII(fatiar3)
        document.getElementById("kds_asci_index").value = convert7

        //Dataset BDS (0x164)
    var getBdsData = '';
    var getBdsindex = '';
        for ( var x = 4246; x < 4254; x++){
            getBdsData +=  document.getElementById(x).innerHTML
        }
        for ( var x =4254; x < 4256; x++){
            getBdsindex +=  document.getElementById(x).innerHTML
        }
        document.getElementById("bds_number").value = getBdsData;
        document.getElementById("bds_index").value = getBdsindex;

        var fatiar3 = '';
        var end3 = 2;
         for(x=0;x<getBdsData.length;x+=2){
            fatiar3 += getBdsData.slice(x,end3);
            fatiar3 += ' ';
            end3 += 2;
        }     
        let convert8 = convertHexToASCII(fatiar3)
        document.getElementById("bds_asci_number").value = convert8

        var fatiar3 = '';
        var end3 = 2;
         for(x=0;x<getBdsindex.length;x+=2){
            fatiar3 += getBdsindex.slice(x,end3);
            fatiar3 += ' ';
            end3 += 2;
        }
        let convert9 = convertHexToASCII(fatiar3)
        document.getElementById("bds_asci_index").value = convert9

    //EngSpeedY()
        var engY = '';
        var arrayEngY =[];
        var getTwoBytes = 1;
        var addresArrayEngY = 0;
        let valueHexEngY=['engY_hex_0','engY_hex_1','engY_hex_2','engY_hex_3']
        let valueDecEngY=['engY_dec_0','engY_dec_1','engY_dec_2','engY_dec_3']
        for (x=1063;x<1071;x++){

            arrayEngY.unshift(document.getElementById(x).innerHTML);    
            if (getTwoBytes == 2){ // SÓ ENTRA NESSE IF SE ESTIVER 2 BYTES NO ARRAY
                engY += arrayEngY[0];
                engY += arrayEngY[1];
                document.getElementById(valueHexEngY[addresArrayEngY]).value = engY;
                engY = parseInt(engY,16)
                document.getElementById(valueDecEngY[addresArrayEngY]).value = engY;
                arrayEngY = []
                getTwoBytes = 0;
                addresArrayEngY+=1
                engY = '';
            }
            getTwoBytes++; 
        }    
        //VehicleSpeedY()
        var espY = '';
        var arrayEspY =[];
        var getTwoBytes = 1;
        var addresArrayEspY = 0;
        let valueHexEspY=['speedY_hex_0','speedY_hex_1','speedY_hex_2','speedY_hex_3','speedY_hex_4']
        let valueDecEspY=['speedY_dec_0','speedY_dec_1','speedY_dec_2','speedY_dec_3','speedY_dec_4']
        for (x=1028;x<1038;x++){

            arrayEspY.unshift(document.getElementById(x).innerHTML);    
            if (getTwoBytes == 2){ // SÓ ENTRA NESSE IF SE ESTIVER 2 BYTES NO ARRAY
                espY += arrayEspY[0];
                espY += arrayEspY[1];
                document.getElementById(valueHexEspY[addresArrayEspY]).value = espY;
                espY = parseInt(espY,16)
                document.getElementById(valueDecEspY[addresArrayEspY]).value = espY;
                arrayEspY = []
                getTwoBytes = 0;
                addresArrayEspY+=1
                espY = '';
            }
            getTwoBytes++;           

        }      
}
//#endregion

//#region Function convert Hex to Ascii
function convertHexToASCII(hexString){
    let stringOut = '';
    hexString.split(' ').map((i) => {
    tempAsciiCode = parseInt(i, 16);
    stringOut = stringOut + String.fromCharCode(tempAsciiCode);
    });
    return stringOut.slice(0,-1)
}
//#endregion

//#region function button html dataset
function js_dSet(){
 eel.dataSet()
 }
//#endregion

//#region LoadDump
function loadDump(){
    limpar()
    eel.dumpHtml()
}
//#endregion

//#region canoe
function canoe(){
    document.getElementById("bt").innerHTML = "VC CLICKOU !"
    eel.automatico()
}
//#endregion

//#region limpar
function limpar(){
    var arrayLimpa = 
    ["ECUSerialNumberDec","ECUSerialNumber","FCA_SW_Number","FCA_SW_NumberDec","FCA_HW_Number","FCA_HW_NumberDec","EcuIdentFiatSparePartNo_number",
    "EcuIdentFiatSparePartNo_Dec","EcuIdentEcuHWNo_number","EcuIdentEcuHWNo_Dec","ApplDataFingerprint_number",
    "ApplDataFingerprint_Dec","ApplSWFingerprint_number","ApplSWFingerprint_Dec","BootSWFingerprint_number",
    "BootSWFingerprint_Dec","DataSet_number","DataSet_index_number","DataSet_Asci_number","DataSet_Asci_index",
    "kds_number","kds_index","kds_asci_number","kds_asci_index","engY_hex_0","engY_dec_0","engY_hex_1",
    "engY_dec_1","engY_hex_2","engY_dec_2","engY_hex_3","engY_dec_3","speedY_hex_0","speedY_dec_0","speedY_hex_1",
    "speedY_dec_1","speedY_hex_2","speedY_dec_2","speedY_hex_3","speedY_dec_3","speedY_hex_4","speedY_dec_4",
    "bds_number","bds_index","bds_asci_number","bds_asci_index"];
     
    for(var i=0; i<8288;i++){ // 4112
    //document.getElementById(i).style.backgroundColor = 'white' ;
    document.getElementById(i).style.backgroundColor = '#92a8d1';
    document.getElementById(i).style.color = "black";
    document.getElementById(i).innerHTML= "";
    document.getElementById('path').innerHTML = 'path Dump:'
    document.getElementById('dSet').innerHTML = 'path DatSet:'
     }

    for(var x=0;x<arrayLimpa.length;x++)
     document.getElementById(arrayLimpa[x]).value= "";  
      
}
//#endregion

//#region js_setPathDump
eel.expose(js_setPathDump);
function js_setPathDump(paths){
     document.getElementById('path').innerHTML = paths
    }
//#endregion

//#region js_setPathDataSet
eel.expose(js_setPathDataSet);
function js_setPathDataSet(paths){
     document.getElementById('dSet').innerHTML = paths
    }

//#endregion

//#region js_imprimirHex
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
//#endregion

//#region js_imprimirHexSeForDiferente
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

 //#endregion
