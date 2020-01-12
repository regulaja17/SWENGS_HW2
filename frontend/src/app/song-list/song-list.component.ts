import { Component, OnInit } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {GenreService} from '../service/genre.service';
import {LabelService} from '../service/label.service';
import {Observable} from 'rxjs';
import {ToastrService} from 'ngx-toastr';

@Component({
  selector: 'app-song-list',
  templateUrl: './song-list.component.html',
  styleUrls: ['./song-list.component.scss']
})
export class SongListComponent implements OnInit {
  songs: any[];
  displayedColumns = ['title', 'genre', 'producer', 'label', 'id'];

  constructor(private http: HttpClient, public genreService: GenreService, private labelService: LabelService,
              private toastr: ToastrService) { }

  ngOnInit() {
    this.http.get('api/song/list').subscribe((response: any[]) => {
      this.songs = response;
    });


  }

  deleteSong(song: any) {
    this.http.get('api/song/' + song.id + '/delete').subscribe( () => {
      this.toastr.success('Song ' + song.title + ' deleted successfully', '', {closeButton: true});
      this.ngOnInit();
    });
  }

}
