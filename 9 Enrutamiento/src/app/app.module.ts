import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { InicioComponent } from './modules/general/inicio/inicio.component';
import { ContactoComponent } from './modules/general/contacto/contacto.component';
import { InformacionComponent } from './modules/general/informacion/informacion.component';
import { IngresarComponent } from './modules/general/ingresar/ingresar.component';
import { NoEncontradoComponent } from './modules/general/no-encontrado/no-encontrado.component';
import { AppRoutingModule } from './app-routing.module';

@NgModule({
  declarations: [
    AppComponent,
    InicioComponent,
    ContactoComponent,
    InformacionComponent,
    IngresarComponent,
    NoEncontradoComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
