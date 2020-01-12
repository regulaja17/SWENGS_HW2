import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {SongListComponent} from './song-list/song-list.component';
import {SongFormComponent} from './song-form/song-form.component';
import {MusicianListComponent} from './musician-list/musician-list.component';
import {MusicianFormComponent} from './musician-form/musician-form.component';
import {LoginComponent} from './login/login.component';
import {AuthGuard} from './guard/auth.guard';


const routes: Routes = [
  { path: '', redirectTo: 'song-list', pathMatch: 'full'},
  { path: 'song-list', component: SongListComponent, canActivate: [AuthGuard]},
  { path: 'song-form', component: SongFormComponent, canActivate: [AuthGuard]},
  { path: 'song-edit/:id', component: SongFormComponent, canActivate: [AuthGuard]},
  { path: 'musician-list', component: MusicianListComponent, canActivate: [AuthGuard]},
  { path: 'musician-form', component: MusicianFormComponent, canActivate: [AuthGuard]},
  { path: 'musician-edit/:id', component: MusicianFormComponent, canActivate: [AuthGuard]},
  { path: 'login', component: LoginComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
