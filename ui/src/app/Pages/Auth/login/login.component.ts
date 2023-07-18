import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent implements OnInit{
  submitting:Boolean = false;

  loginForm:FormGroup = new FormGroup({
    email:new FormControl(''),
    password: new FormControl('')
  })

  constructor(private formBuilder:FormBuilder) {
  }
  ngOnInit(): void {
    this.loginForm = this.formBuilder.group({
      email:['', Validators.required],
      password:['',Validators.required],
    })
  }

  SignIn(){

  }

}
