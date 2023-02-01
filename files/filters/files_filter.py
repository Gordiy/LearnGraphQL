"""Filter for files."""
from common.filters import FilesAndFolderCommonFilter
from files.models import Files


class FilesFilter(FilesAndFolderCommonFilter):
    """Filter for files."""
    class Meta:
        model = Files
        fields = ['id', 'name', 'folder']

