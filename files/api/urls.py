

from django.urls import path

from .import views

urlpatterns = [
    path('upload/', views.fileUpload, name='upload-file'),
    path('test/', views.GetTest.as_view(), name='get-test'),
    path('uploadv2/', views.UploadFile.as_view(), name='upload-file-v2')
]