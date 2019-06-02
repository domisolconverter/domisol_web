from django.urls import path
from django.conf.urls import url
from . import views
from . import emailThread

urlpatterns = [
    path('', views.main, name='main'),
    path('uploading/<str:email>', views.process_upload, name='uploading'),
]
