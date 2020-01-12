import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class LabelService {

  constructor(private http: HttpClient) { }

  retrieveLabel() {
    return this.http.get<any[]>('api/label/list');
  }

  retrieveLabelNameWithId(id: any) {
    return this.http.get('api/label/' + id + '/get-single-name');
  }
}
