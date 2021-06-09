function traerdatos(){
    const valorurl= window.location.search;
    const urlparametros = new URLSearchParams(valorurl);    
    var alimento= urlparametros.get('alimento');
    var calorias= urlparametros.get('calorias');
    var grasas= urlparametros.get('grasas');
    var proteinas = urlparametros.get('proteinas');
    var carbohidratos = urlparametros.get('carbohidratos');
    var img = urlparametros.get('image');
    console.log(img)
    document.body.getElementsByClassName('titulo')[0].textContent = alimento;
    document.body.getElementsByClassName('caloria')[0].textContent = calorias;
    document.body.getElementsByClassName('grasa')[0].textContent = grasas;
    document.body.getElementsByClassName('carbohidratos')[0].textContent = carbohidratos;
    document.body.getElementsByClassName('proteinas')[0].textContent = proteinas;
    if (img=='mal') {
        document.body.getElementsByClassName('imagen')[0].innerHTML='<img id="mal" src="icon/iconfinder_icon-57-sad-face_315570.svg" >'    
    } else {
        document.body.getElementsByClassName('imagen')[0].innerHTML='<img src="icon/iconfinder_simpline_60_2305602.svg">'
    }
    

}


