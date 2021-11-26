import { Component, OnInit, Input } from '@angular/core';
import { Router } from '@angular/router';
import { Producto } from '../shared/producto';
import { RestApiService } from "../shared/rest-api.service";
@Component({
  selector: 'app-productos-create',
  templateUrl: './productos-create.component.html',
  styleUrls: ['./productos-create.component.css']
})
export class ProductosCreateComponent implements OnInit {
  @Input() productoDetalle = { nombre: '', precio: 0, descripcion: '' }
  constructor(public restApi: RestApiService,
    public router: Router) {
  }
  ngOnInit(): void {
  }
  addProducto() {
    this.restApi.createProducto(this.productoDetalle).subscribe((data: {}) => {
      this.router.navigate(['/lista-producto'])
    })
  }
}
