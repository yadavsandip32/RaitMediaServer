from django.urls import path
from . import views

urlpatterns = [
    path('<int:ID>', views.play, name='play'),
	path('', views.list, name='list')

]