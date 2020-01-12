import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class MusicianService {

  constructor(private http: HttpClient) { }

  retrieveMusicians() {
    return this.http.get<any[]>('api/musician/list');
  }
}
