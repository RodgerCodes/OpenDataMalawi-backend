import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './Pages/home/home.component';
import { LoginComponent } from './Pages/Auth/login/login.component';
import { RegisterComponent } from  './Pages/Auth/register/register.component';

const routes: Routes = [
  {
    path:'',
    component:HomeComponent
  },
  {
    path:'sign-in',
    component:LoginComponent,
  },
  {
    path:'sign-up',
    component:RegisterComponent,
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
