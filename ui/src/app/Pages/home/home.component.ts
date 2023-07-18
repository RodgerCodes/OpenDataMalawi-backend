import { Component, OnInit } from '@angular/core';
import  { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit{
  submitting:Boolean = false;

  searchForm:FormGroup = new FormGroup({
    searchQuery:new FormControl('')
  })

  constructor(private formBuilder:FormBuilder) {
  }
  ngOnInit(): void {
    this.searchForm = this.formBuilder.group({
      searchQuery:['', Validators.required]
    })
  }

  searchDataset(){

  }

}
