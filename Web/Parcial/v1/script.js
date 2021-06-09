numfila=0;




function editar(fila) {
    var filas = document.getElementsByClassName('tr'); 
numfila=numfila+1;
if(numfila<=1){   

    //obteniendo valores
    var alimento=filas[fila].childNodes[1].textContent;
    var calorias = filas[fila].childNodes[3].textContent;
    var grasas=filas[fila].childNodes[5].textContent;
    var proteinas=filas[fila].childNodes[7].textContent;
    var carbohidratos=filas[fila].childNodes[9].textContent;
    var ok= filas[fila].childNodes[11].lastChild.lastChild.className;
    



    //editando tabla

    filas[fila].childNodes[1].innerHTML = '<input type="text" name="alimento"  value="'+alimento+'">';
    filas[fila].childNodes[3].innerHTML = '<input type="text" name="calorias" value="'+calorias+'">';
    filas[fila].childNodes[5].innerHTML = '<input type="text" name="grasas" value="'+grasas+'">';
    filas[fila].childNodes[7].innerHTML = '<input type="text" name="proteinas" value="'+proteinas+'">';
    filas[fila].childNodes[9].innerHTML = '<input type="text" name="carbohidratos" value="'+carbohidratos+'">';
    
    if (ok=="bien") {
        filas[fila].childNodes[11].innerHTML= '<select  id="select" onclick="valor()"><option value="bien" selected>bien</option><option value="mal">mal</option></select>'    
    }
    else{
        filas[fila].childNodes[11].innerHTML= '<select  id="select" onclick="valor()"><option value="bien" >bien</option><option value="mal" selected>mal</option></select>'         
    }
    
    idvalue = document.getElementById('select').value;
    document.getElementsByClassName('div4')[0].innerHTML='<input type="hidden" name="image" value="'+idvalue+'">';
    document.getElementsByClassName('tr')[fila].childNodes[13].innerHTML = '<span>En edicion</span>';
    document.body.getElementsByClassName('div1')[0].textContent = 'Pulse Aceptar para guardar los cambios o cancelar para anularlos';
    document.body.getElementsByClassName('div2')[0].innerHTML = '<button type="submit" class="boton" id="aceptar" >Aceptar</button>';
    document.body.getElementsByClassName('div3')[0].innerHTML = '<button type="reset" class="boton" id="cancelar" onclick="location.reload()">Cancelar</button>';
    
                
   
}


else{
    alert("Solo se puede editar uno a la vez >:(");
}



}

function valor(){
    
    idvalue = document.getElementById('select').value;
    document.getElementsByClassName('div4')[0].innerHTML='<input type="hidden" name="image" value="'+idvalue+'">';
    document.body.getElementsByClassName('div2')[0].innerHTML = '<button type="submit" class="boton" id="aceptar" >Aceptar</button>';
    document.body.getElementsByClassName('div3')[0].innerHTML = '<button type="reset" class="boton" id="cancelar" onclick="location.reload()">Cancelar</button>';
    
}