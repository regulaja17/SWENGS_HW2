import { Component, OnInit } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {ToastrService} from 'ngx-toastr';

@Component({
  selector: 'app-musician-list',
  templateUrl: './musician-list.component.html',
  styleUrls: ['./musician-list.component.scss']
})
export class MusicianListComponent implements OnInit {
  musicians: any[];
  displayedColumns = ['alias', 'first_name', 'last_name', 'label', 'id'];

  constructor(private http: HttpClient, private toastr: ToastrService) { }

  ngOnInit() {
    this.http.get('api/musician/list').subscribe((response: any[]) => {
      this.musicians = response;
    });
  }

  deleteMusician(musician: any) {
    this.http.get('api/musician/' + musician.id + '/delete').subscribe(() => {
      this.toastr.success('DJ ' + musician.alias + ' deleted successfully', '', {closeButton: true});
      this.ngOnInit();
    });
  }
}
