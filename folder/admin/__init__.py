"""Register admin for Folder model."""
from django.contrib import admin

from folder.models import Folder

admin.site.register(Folder)
