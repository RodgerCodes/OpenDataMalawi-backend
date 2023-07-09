from django.urls import path
from . import views

app_name="user"
urlpatterns = [
   path('', views.SignIn.as_view(), name="get_sign_in")
]