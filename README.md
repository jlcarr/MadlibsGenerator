# MadlibsGenerator
A Python project using Spacy's NLP engine to generate madlibs from given text, web powered by Django and Bootstrap 5.


![Madlibs Generator logo](https://i2.lensdump.com/i/RtI3LC.png)

## Description
Madlibs are small games in which players are given lists of parts of speechi (e.g. noun, verb, etc), and the words they give are inserted into a phrasal template in order to produce silly stories.

Part of speech tagging is a common part of natural language processing, and many tools exist to perform this task automatically. A popular Python library, which offer "industrial strength out-of-the-box" is Spacy.

The goal of this project is to allow users to provide any base text they want (e.g. song choruses, favorite poem stanzas, etc) and use Spacy's PoS tagging and some string manipulation to automatically create a Madlib from the base text, and furthermore provide a link the users to share their Madlibs with friends, and for the friends to be able to play them online.

## References
### Madlibs and NLP
- https://en.wikipedia.org/wiki/Mad_Libs
- https://en.wikipedia.org/wiki/Phrasal_template
- https://en.wikipedia.org/wiki/Part_of_speech
- https://en.wikipedia.org/wiki/Natural_language_processing
- https://en.wikipedia.org/wiki/SpaCy
- https://spacy.io/
### Django
- https://docs.djangoproject.com/en/4.1/intro/tutorial01/
- https://github.com/cdubz/first-django-app
- https://www.docker.com/blog/how-to-build-and-deploy-a-django-based-url-shortener-app-from-scratch/
- https://github.com/aerabi/link-shortener
### Server Setup
- https://www.vultr.com/docs/using-django-with-nginx-postgresql-and-gunicorn-on-ubuntu-20-04/
- https://www.vultr.com/docs/setup-letsencrypt-on-linux
- https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04
- https://stackoverflow.com/questions/20182329/nginx-is-throwing-an-403-forbidden-on-static-files
### Bootstrap
- https://getbootstrap.com/docs/5.0/utilities/spacing/
- https://getbootstrap.com/docs/5.0/forms/layout/
- https://stackoverflow.com/questions/70063399/how-to-align-the-label-and-the-input-at-the-same-line-in-bootstrap-5
- https://getbootstrap.com/docs/5.0/examples/checkout/
