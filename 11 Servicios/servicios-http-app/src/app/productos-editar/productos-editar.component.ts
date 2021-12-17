import { Component, OnInit } from '@angular/core';
import { Producto } from '../shared/producto';
import { ActivatedRoute, Router } from '@angular/router';
import { RestApiService } from "../shared/rest-api.service";

@Component({
  selector: 'app-productos-editar',
  templateUrl: './productos-editar.component.html',
  styleUrls: ['./productos-editar.component.css']
})
export class ProductosEditarComponent implements OnInit {
  id = this.actRoute.snapshot.params['id'];
  productoData: any = {};
  constructor(
    public restApi: RestApiService,
    public actRoute: ActivatedRoute,
    public router: Router
  ) { }

  ngOnInit() { 
    this.restApi.getProducto(this.id).subscribe((data: {}) => {
      this.productoData = data;
    })
  }
    // Actualizar producto
    updateProducto() {
      if(window.confirm('Estás seguro de actualizar el producto?')){
        this.restApi.updateProducto(this.id, this.productoData).subscribe(data => {
          this.router.navigate(['/lista-producto'])
        })
      }
    }

}
