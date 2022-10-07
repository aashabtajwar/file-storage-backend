

from django.urls import path

from .import views

urlpatterns = [
    path('upload/', views.fileUpload, name='upload-file'),
]