import { Component, OnInit } from '@angular/core';
import { from } from 'rxjs';
import{ApiService} from '../../servicio/api/api.service';
import{Router} from '@angular/router';


import{ listaciudadeI } from '../../modelos/listaciudad.interface'

@Component({
  selector: 'app-ciudad',
  templateUrl: './ciudad.component.html',
  styleUrls: ['./ciudad.component.css']
})

export class CiudadComponent implements OnInit {

  ciudades: listaciudadeI[] = [];
  
  constructor(private api:ApiService,private router:Router) { }

  

  ngOnInit(): void {
      this.api.getciudad().subscribe(datos=>{
        this.ciudades=datos;
        
      })
    }
  editarciudad(id: any){
    console.log(id);
    this.router.navigate(['editar-ciudad',id]); 
  }  

  nuevaciudad(){
    this.router.navigate(['add-ciudad']);
  }
  }


