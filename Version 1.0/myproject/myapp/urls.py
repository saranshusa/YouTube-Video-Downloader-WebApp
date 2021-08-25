from django.urls import path
from .  import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generate', views.generate, name='generate'),
    path('download144p', views.download144p, name='download144p')
]