from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index),
    path('book/', book),
    path('genres/<int:genreid>/', genres),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive)
]