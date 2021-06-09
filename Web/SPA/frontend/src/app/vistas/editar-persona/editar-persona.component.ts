import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, FormsModule } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { personaI } from 'src/app/modelos/persona.interface';
import { ApiService } from 'src/app/servicio/api/api.service';

@Component({
  selector: 'app-editar-persona',
  templateUrl: './editar-persona.component.html',
  styleUrls: ['./editar-persona.component.css']
})
export class EditarPersonaComponent implements OnInit {

  constructor(private activeroute:ActivatedRoute,private router:Router,private api:ApiService,private form:FormsModule) { }

  datosper!:personaI;
  editarform=new FormGroup({

    nombre:new FormControl(''),
    apellidos:new FormControl(''),
    documento:new FormControl(''),
    idtipociu:new FormControl(''),
  
  });

  ngOnInit(): void {
    let personaid=this.activeroute.snapshot.paramMap.get('id');

    this.api.getsingleper(personaid).subscribe(datos=>{

      this.datosper=datos;
      console.log(datos)
      this.editarform.setValue({
        'nombre':this.datosper.nombre,
        'apellidos':this.datosper.apellidos,
        'documento':this.datosper.documento,
        'idtipociu':this.datosper.idtipociu,
      
      });

    });


  }

  putform(form:personaI){
    let perid= this.activeroute.snapshot.paramMap.get('id');
    this.api.putper(form,perid).subscribe(datos=>{
      })

  }

  
  eliminarper(){
    let perid= this.activeroute.snapshot.paramMap.get('id');
    let data:personaI=this.editarform.value;
    this.api.deleteper(data,perid).subscribe(datos=>{
     console.log(datos) 
    });
  }

  salir(){
    this.router.navigate(['principal']);
  }

  







}
