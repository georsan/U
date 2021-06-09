import { Component, OnInit } from '@angular/core';
import{ApiService} from '../../servicio/api/api.service';
import{Router} from '@angular/router';

import{listadocumentoI} from '../../modelos/listadocumentos.interface'


@Component({
  selector: 'app-documento',
  templateUrl: './documento.component.html',
  styleUrls: ['./documento.component.css']
})
export class DocumentoComponent implements OnInit {
 
  documentos:listadocumentoI[]=[];

  constructor(private api:ApiService,private router:Router) { }

  ngOnInit(): void {
    this.api.getdocumento().subscribe(datos=>{
      this.documentos=datos;

    })
  }


  editardocumento(id: any){
    console.log(id);
    this.router.navigate(['editar-documento',id]); 
  }  

  nuevodoc(){
    
    this.router.navigate(['add-documento'])
  }

}
