
var edita=false;


var form= document.getElementById('formulario');
function editar(fila) {

if(edita==false){  
    var nodetr= fila.parentNode;
    var nodetd=nodetr.firstElementChild;
    var form= document.getElementById('formulario');
    var nodestr= nodetr.getElementsByTagName('td');
    //obtener valores
    var alimento=nodestr[0].textContent;
    var calorias=nodestr[1].textContent;
    var grasas=nodestr[2].textContent;
    var proteinas=nodestr[3].textContent;
    var carbohidrato=nodestr[4].textContent;
    var select =nodestr[5].lastChild.lastChild.className;
    console.log(select)

    if (select=='bien') {
        var codigohtml='<td><input type="text" name="alimento"  value="'+alimento+'"></td>'+
        '<td><input type="text" name="calorias"  value="'+calorias+'"></td>'+
        '<td><input type="text" name="grasas"  value="'+grasas+'"></td>'+
        '<td><input type="text" name="proteinas"  value="'+proteinas+'"></td>'+
        '<td><input type="text" name="carbohidratos"  value="'+carbohidrato+'">'+
        '<td><select id="select" onclick="valor()" ><option value="bien" selected>Bien</option><option value="mal">Mal</option></select></td></td><td><span>En edicion</span></td>'
        
    } else {
        var codigohtml='<td><input type="text" name="alimento"  value="'+alimento+'"></td>'+
        '<td><input type="text" name="calorias"  value="'+calorias+'"></td>'+
        '<td><input type="text" name="grasas"  value="'+grasas+'"></td>'+
        '<td><input type="text" name="proteinas"  value="'+proteinas+'"></td>'+
        '<td><input type="text" name="carbohidratos"  value="'+carbohidrato+'">'+
        '<td><select id="select" onclick="valor()" ><option value="bien">Bien</option><option value="mal" selected>Mal</option></select></td></td><td><span>En edicion</span></td>'
            
    }

        
           
    nodetr.innerHTML=codigohtml;

    form.innerHTML='<div class="div1">Pulse Aceptar para guardar los cambios o cancelar para anularlos</div>'+
    '<button type="submit" class="boton" id="aceptar" >Aceptar</button>'+
    '<button type="reset" class="boton" id="cancelar" onclick="location.reload()">Cancelar</button><input type="hidden" name="image"  value="'+select+'"></input>'


    edita=true;
}
    

else{
    alert("Solo se puede editar uno a la vez >:(");
}



}

function valor(){
    
    idvalue = document.getElementById('select').value;
    console.log(idvalue)
    form.innerHTML='<div class="div1">Pulse Aceptar para guardar los cambios o cancelar para anularlos</div>'+
    '<button type="submit" class="boton" id="aceptar" >Aceptar</button>'+
    '<button type="reset" class="boton" id="cancelar" onclick="location.reload()">Cancelar</button>'+
    '<input type="hidden" name="image"  value="'+idvalue+'"></input>'
   
}