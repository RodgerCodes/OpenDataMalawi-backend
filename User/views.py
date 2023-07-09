from django.shortcuts import render
from django.views import View


class SignIn(View):
    def get(self, request):
        return render(request, "Account/Auth/login.html")
