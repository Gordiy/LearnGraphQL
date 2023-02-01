"""Filter class for files and folder apps."""
import django_filters


class FilesAndFolderCommonFilter(django_filters.FilterSet):
    """Filter class for files and folder apps."""
    name = django_filters.CharFilter(lookup_expr='iexact')
    folder__name = django_filters.CharFilter(lookup_expr='iexact')
