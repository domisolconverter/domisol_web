from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('uploading/', views.process_upload, name='uploading'),
]
