import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ComponentMiniComponent } from './component-mini.component';

describe('ComponentMiniComponent', () => {
  let component: ComponentMiniComponent;
  let fixture: ComponentFixture<ComponentMiniComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ComponentMiniComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ComponentMiniComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
