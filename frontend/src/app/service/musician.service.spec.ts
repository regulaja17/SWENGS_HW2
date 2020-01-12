import { TestBed } from '@angular/core/testing';

import { MusicianService } from './musician.service';

describe('MusicianService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: MusicianService = TestBed.get(MusicianService);
    expect(service).toBeTruthy();
  });
});
