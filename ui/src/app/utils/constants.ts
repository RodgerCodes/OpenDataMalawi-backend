import {HttpHeaders} from "@angular/common/http";

let apiUrl = "http://127.0.0.1:8000"
let token = localStorage.getItem("bearer_token");



const setToken = (token:string) => {
  const tokenString:string = JSON.stringify(token);
   localStorage.setItem("bearer_token", tokenString);
};

const getToken = () => {
  let bearer_token;
  if(token != null){
    bearer_token = token;
  }

  return bearer_token;
}

const httpHeaders = {
   headers: new HttpHeaders({
     'Content-Type':'application/json',
     'Authorization': `Bearer ${getToken()}`
   })
}


export   {
  apiUrl,
  setToken,
  getToken,
  httpHeaders,
}
