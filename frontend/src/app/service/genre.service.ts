import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class GenreService {
  genreNames = {
    C: 'Crossbreed',
    D: 'Drumstep',
    J: 'Jump up',
    L: 'Liquid',
    N: 'Neurofunk',
    O: 'Other'
  };

  constructor() { }
}
