import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import {FormsModule,ReactiveFormsModule} from '@angular/forms'
import { AppRoutingModule} from './app-routing.module';
import { AppComponent } from './app.component';
import { PrincipalComponent } from './vistas/principal/principal.component';
import { CiudadComponent } from './vistas/ciudad/ciudad.component';
import { DocumentoComponent } from './vistas/documento/documento.component';
import { AddPersonaComponent } from './vistas/add-persona/add-persona.component';
import { AddCiudadComponent } from './vistas/add-ciudad/add-ciudad.component';
import { AddDocumentoComponent } from './vistas/add-documento/add-documento.component';
import { EditarPersonaComponent } from './vistas/editar-persona/editar-persona.component';
import { EditarDocumentoComponent } from './vistas/editar-documento/editar-documento.component';
import { EditarCiudadComponent } from './vistas/editar-ciudad/editar-ciudad.component';

import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { ToastrModule } from 'ngx-toastr';
import {HttpClientModule} from '@angular/common/http';
import { from } from 'rxjs';






@NgModule({
  declarations: [
    AppComponent,
    PrincipalComponent,
    CiudadComponent,
    DocumentoComponent,
    AddPersonaComponent,
    AddCiudadComponent,
    AddDocumentoComponent,
    EditarPersonaComponent,
    EditarDocumentoComponent,
    EditarCiudadComponent,
    
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    BrowserAnimationsModule, // required animations module
    ToastrModule.forRoot(), // ToastrModule added
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
