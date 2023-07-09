import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './layout/header/header.component';
import { FooterComponent } from './layout/footer/footer.component';
import { HomeComponent } from './Pages/home/home.component';
import { LoginComponent } from './Pages/Auth/login/login.component';
import { RegisterComponent } from './Pages/Auth/register/register.component';
import { ExploreComponent } from './Pages/explore/explore.component';
import { SearchResultsComponent } from './Pages/search-results/search-results.component';
import { BaseComponent } from './Pages/Dashboard/base/base.component';
import { AddDatasetComponent } from './Pages/Dashboard/add-dataset/add-dataset.component';
import { EditDatasetComponent } from './Pages/Dashboard/edit-dataset/edit-dataset.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    FooterComponent,
    HomeComponent,
    LoginComponent,
    RegisterComponent,
    ExploreComponent,
    SearchResultsComponent,
    BaseComponent,
    AddDatasetComponent,
    EditDatasetComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
