"""Model for Files entity."""
from django.db import models
from folder.models import Folder


class Files(models.Model):
    """Model for Files entity."""
    MAX_LENGTH = {
        'NAME': 100,
        'PATH': 200
    }

    name = models.CharField(max_length=MAX_LENGTH['NAME'])
    path = models.CharField(max_length=MAX_LENGTH['PATH'])
    folder = models.ForeignKey(Folder, on_delete=models.SET(Folder.ROOT_FOLDER_ID))
