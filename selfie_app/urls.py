from django.urls import path
from . import views

urlpatterns = [
    path('', views.selfie_view, name='selfie'),
    path('upload/', views.upload_selfie, name='upload_selfie'),
]
