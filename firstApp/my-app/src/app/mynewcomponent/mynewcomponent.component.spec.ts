import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MynewcomponentComponent } from './mynewcomponent.component';

describe('MynewcomponentComponent', () => {
  let component: MynewcomponentComponent;
  let fixture: ComponentFixture<MynewcomponentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MynewcomponentComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(MynewcomponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
