from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_file, name='upload_file'),
    path('access/<str:code>/', views.access_file, name='access_file'),
    path('search/', views.search_code, name='search_code'),
]
