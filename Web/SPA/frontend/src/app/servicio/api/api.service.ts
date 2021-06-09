import { Injectable } from '@angular/core';
import{listaciudadeI} from '../../modelos/listaciudad.interface';
import {HttpClient,HttpHeaders} from '@angular/common/http'
import { Observable} from 'rxjs';
import{CiudadI} from '../../modelos/ciudad.interface'
import { ResponseI } from 'src/app/modelos/response.interface';
import { listadocumentoI } from 'src/app/modelos/listadocumentos.interface';
import { documentoI } from 'src/app/modelos/documentos.interface';
import { listapersonaI } from 'src/app/modelos/listapersoan.interface';
import { personaI } from 'src/app/modelos/persona.interface';




@Injectable({
  providedIn: 'root'
})

export class ApiService {

  url:string="http://127.0.0.1:5000";

  constructor(private http:HttpClient) {}

  
  getciudad():Observable<listaciudadeI[]>{


    let direccion = this.url +'/ciudades' ;
    return this.http.get<listaciudadeI[]>(direccion); 
  }

  getsingleciudad(id: any):Observable<CiudadI>{

    let direccion = this.url + '/ciudades/'+id;

    return this.http.get<CiudadI>(direccion);

  }

  putciudad(form:CiudadI,id:any):Observable<ResponseI>{
    let direccion = this.url + '/ciudades/'+id;
    return this.http.put<ResponseI>(direccion,form);
  }

  deleteciudad(form:CiudadI,id:any):Observable<ResponseI>{
    let direccion = this.url + '/ciudades/'+id;
    
    return this.http.delete<ResponseI>(direccion,{
      headers: new HttpHeaders({ 'Content-Type': 'application/json' })})
  }


  postciudad(form:CiudadI):Observable<ResponseI>{
    let direccion = this.url + '/ciudades';

    return this.http.post<ResponseI>(direccion,form);

  }

  
///////////////////////////////////////////////////////////////////

getdocumento():Observable<listadocumentoI[]>{


  let direccion = this.url +'/document' ;
  return this.http.get<listadocumentoI[]>(direccion); 
}

getsingledoc(id: any):Observable<documentoI>{

  let direccion = this.url + '/document/'+id;

  return this.http.get<documentoI>(direccion);

}

putdocument(form:documentoI,id:any):Observable<ResponseI>{
  let direccion = this.url + '/document/'+id;
  return this.http.put<ResponseI>(direccion,form);
}

deletedoc(form:documentoI,id:any):Observable<ResponseI>{
  let direccion = this.url + '/document/'+id;
  
  return this.http.delete<ResponseI>(direccion,{
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })})
}


postdoc(form:documentoI):Observable<ResponseI>{
  let direccion = this.url + '/document';

  return this.http.post<ResponseI>(direccion,form);

}

/////////////////////////////////////////////////////////////
getpersona():Observable<listapersonaI[]>{


  let direccion = this.url +'/persona' ;
  return this.http.get<listapersonaI[]>(direccion); 
}

getsingleper(id:any):Observable<personaI>{

  let direccion = this.url + '/persona/'+id;
  console.log(id)
  return this.http.get<personaI>(direccion);

}

putper(form:personaI,id:any):Observable<ResponseI>{
  let direccion = this.url + '/persona/'+id;
  return this.http.put<ResponseI>(direccion,form);
}

deleteper(form:personaI,id:any):Observable<ResponseI>{
  let direccion = this.url + '/persona/'+id;
  
  return this.http.delete<ResponseI>(direccion,{
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })})
}


postper(form:personaI):Observable<ResponseI>{
  let direccion = this.url + '/persona';

  return this.http.post<ResponseI>(direccion,form);

}




} 
