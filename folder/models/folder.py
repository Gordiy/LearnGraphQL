"""Model for Folder entity."""
from django.db import models


class Folder(models.Model):
    """Model for Folder entity."""
    FOLDER_MAX_LENGTH = 50
    ROOT_FOLDER_ID = 1

    name = models.CharField(max_length=50, default='New folder', null=False)
    previous = models.ForeignKey('self', on_delete=models.SET(ROOT_FOLDER_ID))
    
