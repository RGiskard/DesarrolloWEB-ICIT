import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-ingresar',
  templateUrl: './ingresar.component.html',
  styleUrls: ['./ingresar.component.css']
})
export class IngresarComponent implements OnInit {

  constructor() { }
  saludo:string="Hola bienvenido";
  edad:number=18;
  ngOnInit(): void {
  }

}
