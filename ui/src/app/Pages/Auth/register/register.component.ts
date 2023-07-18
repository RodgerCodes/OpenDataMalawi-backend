import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit{
  submitting:Boolean = false;

  registerForm:FormGroup = new FormGroup({
    username:new FormControl(''),
    email: new FormControl(''),
    password: new FormControl(''),
  })

  constructor(private formBuilder:FormBuilder) {
  }
  ngOnInit(): void {
    this.registerForm = this.formBuilder.group({
      username:['', Validators.required],
      email:['', Validators.required],
      password:['', Validators.required],
    })
  }

}
