from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView

from .models import BaseText, Substitution

from . import madlibs

def index(request):
	return render(request, 'main/index.html')


def generate_madlib(request):
	text = request.POST['basetext']
	basetext, substitutions = madlibs.generate_madlib(text)
	basetext_obj = BaseText(text=basetext)
	basetext_obj.save()
	for (sub_lemma, sub_pos),sub_swap_id in substitutions.items():
		substitution_obj = basetext_obj.substitution_set.create(swap_id=sub_swap_id, pos=sub_pos, lemma=sub_lemma)
		substitution_obj.save()
	context = {
		'basetext': basetext_obj,
		'substitution_set': basetext_obj.substitution_set.all(),
	}
	return render(request, "main/generation.html", context)


class Play(TemplateView):
	def get(self, request, madlib_id):
		basetext = get_object_or_404(BaseText, pk=madlib_id)
		substitution_set = basetext.substitution_set.all()
		context = {
			'basetext': basetext,
			'substitution_list': substitution_set,
		}
		return render(request, "main/play.html", context)

	def post(self, request, madlib_id):
		basetext = get_object_or_404(BaseText, pk=madlib_id)
		substitutions = {}
		for substitution in basetext.substitution_set.all():
			key = f"swap-{substitution.swap_id}"
			if key not in request.POST:
				return HttpResponse('Missing sub')
			swap_id = key.split('-')[-1]
			substitutions[swap_id] = request.POST[key]
		context = {
			'text': madlibs.sub_inflected(basetext.text, substitutions),
		}
		return render(request, "main/filled.html", context)
