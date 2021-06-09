import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, FormsModule } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { personaI } from 'src/app/modelos/persona.interface';
import { ApiService } from 'src/app/servicio/api/api.service';

@Component({
  selector: 'app-add-persona',
  templateUrl: './add-persona.component.html',
  styleUrls: ['./add-persona.component.css']
})
export class AddPersonaComponent implements OnInit {
  
  constructor( private activeroute:ActivatedRoute,private router:Router,private api:ApiService,private form:FormsModule) { }

  nuevoform=new FormGroup({

    nombre:new FormControl(''),
    apellidos:new FormControl(''),
    idtipodoc:new FormControl(''),
    documento:new FormControl(''),
    idtipociu:new FormControl(''),
    fechanacimiento:new FormControl(''),
    email:new FormControl(''),
    telefono:new FormControl(''),
    usuario:new FormControl(''),
    password:new FormControl(''),
  });

    

  ngOnInit(): void {
  }

  postform(form:personaI){
    this.api.postper(form).subscribe(datos=>{
      console.log(datos);
    });
  } 

}
