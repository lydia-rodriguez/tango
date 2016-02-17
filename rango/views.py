from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response


def index (request):
	return render_to_response ('rango/index.html')
	
def about (request):
	return render_to_response ('rango/about.html')
	
def contact_us (request):
	context = RequestContext (request)
	context_dict = {'boldmessage': "Contact Us anytime!"}
	return render_to_response ('rango/contactUs.html', context_dict, context)