import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {Observable} from "rxjs";
import { apiUrl } from '../../utils/constants';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private http:HttpClient) { }


  register(formData:any):Observable<any>{
    return this.http.post(`${apiUrl}/api/account/v1/register/`, formData)
  }

  login(formData:any):Observable<any>{
     return this.http.post(`${apiUrl}/api/account/v1/login/`, formData)
  }
}
