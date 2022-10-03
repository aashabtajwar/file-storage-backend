

from django.urls import path

from .import views

urlpatterns = [
    path('register/', views.userRegistration, name='register'),
    path('login/', views.userLogin, name='user-login'),
    path('test/', views.testRoute, name='test')
]