import pandas as pd
import numpy as np

import re

import spacy
import pyinflect
from spacy import displacy
nlp = spacy.load("en_core_web_sm")


def is_madlib(token):
    if (token.pos_ == 'PROPN'):
        return 0.9
    if (token.pos_ == 'NUM'):
        return 0.95
    if (token.pos_ == 'ADV'):
        return 0.9
    if (token.pos_ == 'ADJ'):
        return 0.9
    if (token.dep_ == 'amod'):
        return 0.7
    if (token.pos_ == 'NOUN' and token.dep_ == 'dobj'):
        return 0.4
    if (token.pos_ == 'NOUN' and token.dep_ == 'pobj'):
        return 0.5
    if (token.pos_ == 'NOUN' and token.dep_ == 'nsubj'):
        return 0.7
    if (token.pos_ == 'NOUN' and token.dep_ == 'compound'):
        return 0.1
    if (token.pos_ == 'VERB' and not (token.dep_ == 'ccomp' or any([sub_token.dep_ == 'ccomp' for sub_token in token.subtree]))):
        return 0.7
    return 0.0

def generate_madlib(text):
	text = text.replace('{', '').replace('}', '')

	doc = nlp(text)
	
	df = pd.DataFrame([
		{
			'text': token.text,
			'lemma': token.lemma_,
			'POS': token.pos_,
			'tag': token.tag_,
			'dep': token.dep_,
			'shape': token.shape_,
			'is_alpha': token.is_alpha,
			'is_stop': token.is_stop,
			'madlib_prob': is_madlib(token)
		}
		for token in doc
	])

	df.drop_duplicates(subset=['lemma','POS'], inplace=True)
	df = df[df['madlib_prob'] > np.random.rand(len(df))]
	df.reset_index(inplace=True)
	
	replacement_dict = {(row['lemma'], row['POS']):i for i,row in df.iterrows()}

	result_text = ''
	for token in doc:
		lemma, pos, tag = token.lemma_, token.pos_, token.tag_
		if (lemma, pos) in replacement_dict:
			 result_text += '{' + str(replacement_dict[(lemma, pos)]) + ',' + tag + '}'
		else:
			result_text += str(token)
		result_text += token.whitespace_

	return result_text, replacement_dict

def sub_inflected(basetext, substitutions):
	found_substitutions = re.findall(r'\{(\d+),(\w+)\}', basetext)
	for swap_id,tag in found_substitutions:
		if swap_id not in substitutions:
			return None
		base_replacement = substitutions[swap_id]
		new_token = base_replacement
		if tag not in ['PRP', 'NNP', 'NNPS', 'CD']:
			base_replacement = base_replacement.lower()
			new_token = nlp(base_replacement)[0]._.inflect(tag)
			if not new_token:
				new_token = base_replacement
		basetext = basetext.replace('{' + swap_id + ',' + tag + '}', new_token)
	return basetext

