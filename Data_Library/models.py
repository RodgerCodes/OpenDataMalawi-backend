from django.db import models
from .Paths.upload_paths import get_file_format_logo_path, get_dataset_file_path


class FileFormat(models.Model):
    name = models.CharField(max_length=600)
    imagePath = models.ImageField(
        upload_to=get_file_format_logo_path, null=True, blank=True
    )

    def __str__(self):
        return self.name


class Field(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Dataset(models.Model):
    title = models.CharField(max_length=600)
    field = models.ForeignKey(Field, on_delete=models.SET_NULL, null=True, blank=True)
    uploadedBy = models.ForeignKey(
        "User.User", on_delete=models.SET_NULL, null=True, blank=True
    )
    fileType = models.ForeignKey(
        FileFormat, on_delete=models.SET_NULL, null=True, blank=True
    )
    filePath = models.FileField(upload_to=get_dataset_file_path)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title
