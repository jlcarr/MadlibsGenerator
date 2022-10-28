from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:madlib_id>/', views.play_madlib, name='play'),
	path('<int:madlib_id>/fill/', views.fill_madlib, name='fill'),
	path('generate', views.generate_madlib, name='generate_madlib'),
]
