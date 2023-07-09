from django.urls import path
from . import views

app_name = "user"
urlpatterns = [
    path('', views.SignIn.as_view(), name="sign_in"),
    path('register/', views.SignUp.as_view(), name="sign_up")
]
