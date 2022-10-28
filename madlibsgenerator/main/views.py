from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import BaseText

def index(request):
	return render(request, 'main/index.html')

def generate_madlib(request):
	return HttpResponse(request.POST['basetext'])


def play_madlib(request, madlib_id):
	basetext = get_object_or_404(BaseText, pk=madlib_id)
	substitution_set = basetext.substitution_set.all()
	context = {
		'basetext': basetext,
		'substitution_list': substitution_set,
	}
	return render(request, "main/play.html", context)

def fill_madlib(request, madlib_id):
	basetext = get_object_or_404(BaseText, pk=madlib_id)
	context = {
		'text': basetext.text,
	}
	return render(request, "main/filled.html", context)
