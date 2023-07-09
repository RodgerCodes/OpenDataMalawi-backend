from django.urls import path
from . import views

app_name = "user"
urlpatterns = [
    path('v1/register/', views.RegisterAccount.as_view())
]
