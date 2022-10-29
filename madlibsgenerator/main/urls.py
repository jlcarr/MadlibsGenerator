from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
	path('', views.index, name='index'),
	path('play/<int:madlib_id>/', views.Play.as_view(), name='play'),
	path('generate', views.generate_madlib, name='generate'),
]
