from django.shortcuts import render
from django.http import HttpResponse

from .models import BaseText

def index(request):
	return render(request, 'main/index.html')

def generate_madlib(request):
	return HttpResponse(request.POST['basetext'])

def play_madlib(request, madlib_id):
	substitution_set = BaseText.objects.get(pk=madlib_id).substitution_set.all()
	return HttpResponse(str([s.__str__() for s in substitution_set]))
