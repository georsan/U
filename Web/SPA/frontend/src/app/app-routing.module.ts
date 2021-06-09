import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { from } from 'rxjs';
import {AddCiudadComponent} from './vistas/add-ciudad/add-ciudad.component'
import {AddDocumentoComponent} from './vistas/add-documento/add-documento.component'
import {AddPersonaComponent} from './vistas/add-persona/add-persona.component'
import {CiudadComponent} from './vistas/ciudad/ciudad.component'
import {DocumentoComponent} from './vistas/documento/documento.component'
import {EditarCiudadComponent} from './vistas/editar-ciudad/editar-ciudad.component'
import {EditarDocumentoComponent} from './vistas/editar-documento/editar-documento.component'
import {EditarPersonaComponent} from './vistas/editar-persona/editar-persona.component'
import {PrincipalComponent} from './vistas/principal/principal.component'

const routes: Routes = [
  {path:'',redirectTo:'principal',pathMatch:'full'},
  {path:'principal',component:PrincipalComponent},
  {path:'editar-persona/:id',component:EditarPersonaComponent},
  {path:'editar-documento/:id',component:EditarDocumentoComponent},
  {path:'editar-ciudad/:id',component:EditarCiudadComponent},
  {path:'documento',component:DocumentoComponent},
  {path:'ciudad',component:CiudadComponent},
  {path:'add-persona',component:AddPersonaComponent},
  {path:'add-documento',component:AddDocumentoComponent},
  {path:'add-ciudad',component:AddCiudadComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

export const routingComponentes={PrincipalComponent,DocumentoComponent,CiudadComponent,AddPersonaComponent,AddDocumentoComponent,AddCiudadComponent}

//export const routingComponentesadd={EditarPersonaComponent,EditarDocumentoComponent,EditarCiudadComponent}