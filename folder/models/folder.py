"""Model for Folder entity."""
from django.db import models


class Folder(models.Model):
    """Model for Folder entity."""
    FOLDER_MAX_LENGTH = 50
    ROOT_FOLDER_ID = 1
    DEFAULT_FOLDER_NAME = 'New folder'

    name = models.CharField(max_length=50, default=DEFAULT_FOLDER_NAME, null=False)
    previous = models.ForeignKey('self', on_delete=models.SET(ROOT_FOLDER_ID), blank=True, null=True)
    
    def __str__(self):
        """Helper method that describe Folder instance."""
        return self.name
