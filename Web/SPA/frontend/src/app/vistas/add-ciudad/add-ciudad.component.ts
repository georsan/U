import { Component, OnInit } from '@angular/core';
import{Router,ActivatedRoute} from '@angular/router';

import { ReactiveFormsModule,FormsModule } from '@angular/forms';
import{ApiService} from '../../servicio/api/api.service';
import{FormGroup,FormControl,Validator} from '@angular/forms';
import { CiudadI } from 'src/app/modelos/ciudad.interface';









@Component({
  selector: 'app-add-ciudad',
  templateUrl: './add-ciudad.component.html',
  styleUrls: ['./add-ciudad.component.css']
})
export class AddCiudadComponent implements OnInit {

  constructor( private activeroute:ActivatedRoute,private router:Router,private api:ApiService,private form:FormsModule) { }

  nuevoform= new FormGroup({
    ciudad: new FormControl(''),
    departamento: new FormControl(''),
  });


  ngOnInit(): void {
  }

  postform(form:CiudadI){
    this.api.postciudad(form).subscribe(datos=>{
      console.log(datos);
    });
  } 
}
