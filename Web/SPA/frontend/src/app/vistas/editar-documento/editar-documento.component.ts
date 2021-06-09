import { Component, OnInit } from '@angular/core';
import { from } from 'rxjs';
import{Router,ActivatedRoute} from '@angular/router';

import { ReactiveFormsModule,FormsModule } from '@angular/forms';
import{ApiService} from '../../servicio/api/api.service';
import{FormGroup,FormControl,Validator} from '@angular/forms';
import { documentoI } from 'src/app/modelos/documentos.interface';

@Component({
  selector: 'app-editar-documento',
  templateUrl: './editar-documento.component.html',
  styleUrls: ['./editar-documento.component.css']
})
export class EditarDocumentoComponent implements OnInit {

  constructor(private activeroute:ActivatedRoute,private router:Router,private api:ApiService,private form:FormsModule) { }

  datodoc!:documentoI;
  editarform=new FormGroup({
    nombre:new FormControl(''),
    descripcion:new FormControl(''),
  });



  ngOnInit(): void {
    let documentoid=this.activeroute.snapshot.paramMap.get('id');

    this.api.getsingledoc(documentoid).subscribe(datos=>{

      this.datodoc=datos;

      this.editarform.setValue({
        'nombre':this.datodoc.nombre,
        'descripcion':this.datodoc.descripcion
      });

    });

  }

  putform(form:documentoI){
    let docid= this.activeroute.snapshot.paramMap.get('id');
    this.api.putdocument(form,docid).subscribe(datos=>{
      })

  }

  
  eliminardoc(){
    let docid= this.activeroute.snapshot.paramMap.get('id');
    let data:documentoI=this.editarform.value;
    this.api.deletedoc(data,docid).subscribe(datos=>{
     console.log(datos) 
    });
  }

  salir(){
    this.router.navigate(['documento']);
  }













}
