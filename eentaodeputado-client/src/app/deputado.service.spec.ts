import { TestBed, inject } from '@angular/core/testing';

import { DeputadoService } from './deputado.service';

describe('DeputadoService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [DeputadoService]
    });
  });

  it('should be created', inject([DeputadoService], (service: DeputadoService) => {
    expect(service).toBeTruthy();
  }));
});
