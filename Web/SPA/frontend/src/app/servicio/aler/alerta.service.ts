import { Injectable } from '@angular/core';
import {ToastrService} from 'ngx-toastr';
@Injectable({
  providedIn: 'root'
})
export class AlertaService {
  [x: string]: any;

  constructor(private alert:ToastrService) { }


  showsucces(texto: any,titulo: any){
    this.toast.succes(texto,titulo);
  }

  showerror(texto: any,titulo: any){
    this.toast.error(texto,titulo);
  }


}
