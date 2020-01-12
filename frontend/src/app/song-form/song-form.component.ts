import {Component, OnInit} from '@angular/core';
import {AbstractControl, FormBuilder, FormControl, ValidationErrors, ValidatorFn, Validators} from '@angular/forms';
import {HttpClient} from '@angular/common/http';
import {ActivatedRoute, Router} from '@angular/router';
import {GenreService} from '../service/genre.service';
import {MusicianService} from '../service/musician.service';
import {LabelService} from '../service/label.service';
import {ToastrService} from 'ngx-toastr';


@Component({
  selector: 'app-song-form',
  templateUrl: './song-form.component.html',
  styleUrls: ['./song-form.component.scss'],
})

export class SongFormComponent implements OnInit {
  musicianOptions;
  labelOptions;
  songFormGroup;

  constructor(private fb: FormBuilder, private http: HttpClient, private route: ActivatedRoute, public genreService: GenreService,
              private musicianService: MusicianService, private labelService: LabelService, private toastr: ToastrService,
              private router: Router) {
  }

  ngOnInit() {
    this.songFormGroup = this.fb.group({
      'id': [null],
      'title': ['', Validators.required],
      'features': ['', this.noNumberValidator()],
      'genre': [null],
      'release_date': [null],
      'duration': [0.00],
      'label': [null],
      'producer': [[]]
    });

    const id = this.route.snapshot.paramMap.get('id');
    if (id) {
      this.http.get('api/song/' + id + '/get').subscribe((response) => {
        this.songFormGroup.patchValue(response);
      });
    }

    this.musicianService.retrieveMusicians().subscribe(result => {
      this.musicianOptions = result;
    });

    this.labelService.retrieveLabel().subscribe(result => {
      this.labelOptions = result;
    });

  }

  createSong() {
    const song = this.songFormGroup.value;
    if (song.id) {
      this.http.put('api/song/' + song.id + '/update', song).subscribe(() => {
        this.toastr.success('Song updated successfully', '', {closeButton: true});
      });
    } else {
      this.http.post('api/song/create', this.songFormGroup.value).subscribe(() => {
        this.toastr.success('Song created successfully', '', {closeButton: true});
      });
    }
    this.router.navigate(['song-list']);
  }

  noNumberValidator(): ValidatorFn {
    return (control: AbstractControl): ValidationErrors | null => {
      const input = control.value as string;
      const regexpNumber: RegExp = /[0-9]/;
      if (input !== '' && regexpNumber.test(input)) {
        return {shouldNotContainNumber: true};
      }
      return null;
    };
  }

}
