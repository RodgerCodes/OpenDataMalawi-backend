from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/account/", include("User.urls")),
    path("api/library/", include("Data_Library.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
