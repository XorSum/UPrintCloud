from django.urls import path
from . import views

urlpatterns = [
    path('upload', views.upload, name='api.upload'), # for test
    path('request', views.request, name='api.request'),
    path('download', views.download, name='api.download'),
]
