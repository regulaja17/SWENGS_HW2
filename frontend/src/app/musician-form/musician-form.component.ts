import {Component, OnInit} from '@angular/core';
import {FormBuilder, Validators} from '@angular/forms';
import {HttpClient} from '@angular/common/http';
import {ActivatedRoute, Router} from '@angular/router';
import {LabelService} from '../service/label.service';
import {ToastrService} from 'ngx-toastr';

@Component({
  selector: 'app-musician-form',
  templateUrl: './musician-form.component.html',
  styleUrls: ['./musician-form.component.scss']
})
export class MusicianFormComponent implements OnInit {
  musicianFormGroup;
  labelOptions;
  yearOptions = [];

  constructor(private fb: FormBuilder, private http: HttpClient, private route: ActivatedRoute, private labelService: LabelService,
              private toastr: ToastrService, private router: Router) {
  }

  ngOnInit() {
    this.musicianFormGroup = this.fb.group({
      'id': [null],
      'alias': ['', Validators.required],
      'first_name': [''],
      'last_name': [''],
      'year_of_birth': [0, Validators.required],
      'label': [[]],
      'active': [true]
    });

    const id = this.route.snapshot.paramMap.get('id');
    if (id) {
      this.http.get('api/musician/' + id + '/get').subscribe(response => {
        this.musicianFormGroup.patchValue(response);
      });
    }

    this.labelService.retrieveLabel().subscribe(response => {
      this.labelOptions = response;
    });

    for (let x = (new Date()).getFullYear(); x >= 1900; x--) {
      this.yearOptions.push(x);
    }
  }

  createMusician() {
    const musician = this.musicianFormGroup.value;
    if (musician.id) {
      this.http.put('api/musician/' + musician.id + '/update', musician).subscribe(() => {
        this.toastr.success('DJ updated successfully', '', {closeButton: true});
      });
    } else {
      this.http.post('api/musician/create', this.musicianFormGroup.value).subscribe(() => {
        this.toastr.success('DJ created successfully', '', {closeButton: true});
      });
    }
    this.router.navigate(['musician-list']);
  }

}
