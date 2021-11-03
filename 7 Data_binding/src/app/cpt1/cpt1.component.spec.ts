import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Cpt1Component } from './cpt1.component';

describe('Cpt1Component', () => {
  let component: Cpt1Component;
  let fixture: ComponentFixture<Cpt1Component>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ Cpt1Component ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(Cpt1Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
