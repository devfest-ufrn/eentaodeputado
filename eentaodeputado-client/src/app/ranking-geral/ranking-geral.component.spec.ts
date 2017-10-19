import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RankingGeralComponent } from './ranking-geral.component';

describe('RankingGeralComponent', () => {
  let component: RankingGeralComponent;
  let fixture: ComponentFixture<RankingGeralComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RankingGeralComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RankingGeralComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
