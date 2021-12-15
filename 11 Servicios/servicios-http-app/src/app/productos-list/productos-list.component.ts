import { Component, OnInit } from '@angular/core';
import { RestApiService } from "../shared/rest-api.service";

@Component({
  selector: 'app-productos-list',
  templateUrl: './productos-list.component.html',
  styleUrls: ['./productos-list.component.css']
})
export class ProductosListComponent implements OnInit {
  Producto: any=[]

  constructor(public restApi: RestApiService) { }

  ngOnInit(): void {
    this.loadProductos()
  }
  loadProductos() {
    return this.restApi.getProductos().subscribe((data: {}) => {
      this.Producto = data;
    })
  }

}
