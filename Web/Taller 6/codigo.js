function __(id){
    return document.getElementById(id);
  }

function validarContraseña() {
    var pass = __('pass').value,
        pass2 = __('pass2').value;
    if(pass != '' && pass2 != ''){
      if(pass != pass2){
        //si las contraseñas no coinciden
    alert("¡Las contraseñas no coinciden!");
    return false;   
    } else {
        //Si todo esta correcto 
    alert("correcot");    
        return true;
}
    } else {
      //si los campos o uno, este vacio
      alert("los campos no coinsiden");    
    
    return false;} 
  }