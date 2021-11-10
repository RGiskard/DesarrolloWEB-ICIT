import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { AppComponent } from './app.component';
import { InicioComponent } from './modules/general/inicio/inicio.component';
import { ContactoComponent } from './modules/general/contacto/contacto.component';
import { InformacionComponent } from './modules/general/informacion/informacion.component';
import { IngresarComponent } from './modules/general/ingresar/ingresar.component';
import { NoEncontradoComponent } from './modules/general/no-encontrado/no-encontrado.component';

const routes: Routes = [
  { path: '', component: InicioComponent, },
  { path: 'contacto', component: ContactoComponent },
  { path: 'informacion', component: InformacionComponent },
  { path: 'ingresar', component: IngresarComponent },
  { path: '**', component: NoEncontradoComponent }
];

@NgModule({
  declarations: [],
  imports: [
    RouterModule.forRoot(routes)
  ],
  exports: [RouterModule],
})
export class AppRoutingModule { }
