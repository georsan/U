import { Component, OnInit } from '@angular/core';
import { from } from 'rxjs';
import{Router,ActivatedRoute} from '@angular/router';

import { ReactiveFormsModule,FormsModule } from '@angular/forms';
import{ApiService} from '../../servicio/api/api.service';
import{FormGroup,FormControl,Validator} from '@angular/forms';
import { CiudadI } from 'src/app/modelos/ciudad.interface';


@Component({
  selector: 'app-editar-ciudad',
  templateUrl: './editar-ciudad.component.html',
  styleUrls: ['./editar-ciudad.component.css']
})
export class EditarCiudadComponent implements OnInit {

  constructor(private activeroute:ActivatedRoute,private router:Router,private api:ApiService,private form:FormsModule) {}
    datociudad!: CiudadI;
    editarform= new FormGroup({
    ciudad: new FormControl(''),
    departamento: new FormControl(''),
  });



  ngOnInit(): void {
    let ciudadid= this.activeroute.snapshot.paramMap.get('id');
    
    this.api.getsingleciudad(ciudadid).subscribe(datos=>{
      console.log(datos);
      this.datociudad= datos;
      this.editarform.setValue({
        'ciudad':this.datociudad.ciudad,
        'departamento':this.datociudad.departamento
      });
      
      console.log(this.editarform.value);

    });
  }

  putform(form:CiudadI){
    let ciudadid= this.activeroute.snapshot.paramMap.get('id');
    this.api.putciudad(form,ciudadid).subscribe(datos=>{
      
       
    })

  }

  eliminarciudad(){
    let ciudadid= this.activeroute.snapshot.paramMap.get('id');
    let data:CiudadI=this.editarform.value;
    this.api.deleteciudad(data,ciudadid).subscribe(datos=>{
     console.log(datos) 
    });
  }

  salir(){
    this.router.navigate(['ciudad']);
  }
}
