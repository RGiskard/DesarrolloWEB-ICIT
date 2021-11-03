import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PrimerComponentComponent } from './primer-component.component';

describe('PrimerComponentComponent', () => {
  let component: PrimerComponentComponent;
  let fixture: ComponentFixture<PrimerComponentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PrimerComponentComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PrimerComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
