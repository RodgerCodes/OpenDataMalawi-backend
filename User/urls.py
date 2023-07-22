from django.urls import path
from . import views

app_name = "user"
urlpatterns = [
    path("v1/register/", views.RegisterAccount.as_view()),
    path("v1/login/", views.MyTokenObtainPairView.as_view()),
    path("v1/account/details/<pk>/", views.GetUserDetails.as_view()),
    path("v1/account/edit/", views.EditUserDetails.as_view()),
]
