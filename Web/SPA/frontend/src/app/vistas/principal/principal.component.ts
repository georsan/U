import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { listapersonaI } from 'src/app/modelos/listapersoan.interface';
import { ApiService } from 'src/app/servicio/api/api.service';

@Component({
  selector: 'app-principal',
  templateUrl: './principal.component.html',
  styleUrls: ['./principal.component.css']
})
export class PrincipalComponent implements OnInit {

  personas: listapersonaI[] = []; 

  constructor(private api:ApiService,private router:Router) { }


  ngOnInit(): void {
    this.api.getpersona().subscribe(datos=>{
      
      this.personas=datos;

    })
  }

  nuevaper(){

    this.router.navigate(['add-persona']);
  }



  editarpers(id:any){

    this.router.navigate(['editar-persona',id])
  }








}
