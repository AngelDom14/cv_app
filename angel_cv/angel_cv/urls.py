"""URL configuration for the angel_cv project."""

from django.urls import include, path

urlpatterns = [
    path('', include('portfolio.urls')),
]
