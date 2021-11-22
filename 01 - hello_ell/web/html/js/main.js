

function auto(){
    var e = document.getElementById("selecao");
    var strUser = e.value;
    var nameSalveDump = prompt("Please enter name to save!");
    if (nameSalveDump != null) {
        eel.openProject(strUser,nameSalveDump)
    }
  }

function canoe(){
    var e = document.getElementById("selecao"); 
    var strUser = e.value;
    document.getElementById("ids").innerHTML= "foi";
    document.getElementById("bt").innerHTML = "VC CLICKOU !"
    eel.openCcanoe(strUser)
  
  }

function dialog(){
   windowObjectReference = window.open("multiprompt.html",'','top=120,left=310,resizable=no, width=400,height=150')

  }

 //Fecha a caixa de diálogo sem configurar um valor de retorno
function fail() {
    window.close();

 }

function okay() {
document.getElementById("dSet").innerHTML = "Ramos";
//var e = document.getElementById("labTell").value;

//window.close(); // Fecha a caixa de diálogo.
}