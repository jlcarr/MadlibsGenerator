from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:madlib_id>/', views.play_madlib, name='play'),
	path('generate', views.generate_madlib, name='generate_madlib'),
]
