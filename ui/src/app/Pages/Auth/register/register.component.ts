import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from '../../../Services/Auth/auth.service';

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

  constructor(private formBuilder:FormBuilder, private router:Router, private authService:AuthService) {
  }
  ngOnInit(): void {
    this.createForm();
  }

  createForm(){
      this.registerForm = this.formBuilder.group({
      username:['', Validators.required],
      email:['', Validators.required],
      password:['', Validators.required],
    })
  }

  RegisterUser(){
    if(this.registerForm.valid){
       this.submitting = true;
       this.authService.register(this.registerForm.value).subscribe({
         next: (response) => {

         } ,
         error: (err:any) => {

         }
       })
    } else {

    }
  }

}
