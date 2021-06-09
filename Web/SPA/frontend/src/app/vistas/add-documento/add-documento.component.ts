import { Component, OnInit } from '@angular/core';
import { FormsModule, FormGroup, FormControl } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { documentoI } from 'src/app/modelos/documentos.interface';
import { ApiService } from 'src/app/servicio/api/api.service';

@Component({
  selector: 'app-add-documento',
  templateUrl: './add-documento.component.html',
  styleUrls: ['./add-documento.component.css']
})
export class AddDocumentoComponent implements OnInit {

  constructor( private activeroute:ActivatedRoute,private router:Router,private api:ApiService,private form:FormsModule) { }

  nuevoform= new FormGroup({
    nombre: new FormControl(''),
    descripcion: new FormControl(''),
  });


  ngOnInit(): void {
  }

  postform(form:documentoI){
    this.api.postdoc(form).subscribe(datos=>{
      console.log(datos);
    });
  } 
}
