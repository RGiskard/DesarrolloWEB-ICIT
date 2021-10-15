import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-primer-component',
  templateUrl: './primer-component.component.html',
  styleUrls: ['./primer-component.component.css']
})
export class PrimerComponentComponent implements OnInit {
  public edad:number=18;
  constructor() {
    this.edad = 15;
   }

  ngOnInit(): void {
    
  }

}
