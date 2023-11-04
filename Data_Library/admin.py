from django.contrib import admin
from .models import FileFormat, Field, Dataset

admin.site.register(FileFormat)
admin.site.register(Field)
admin.site.register(Dataset)
