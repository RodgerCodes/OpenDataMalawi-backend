from django.urls import path
from . import views

urlpatterns = [
    path("v1/get-file-formats/", views.GetFileFormat.as_view()),
    path("v1/get-dataset-fields/", views.GetFields.as_view()),
    path("v1/add-dataset/", views.AddDataSet.as_view()),
    path(
        "v1/search-datasets-by-name/<str:searchQuery>/",
        views.SearchDataSetsByName.as_view(),
    ),
]
