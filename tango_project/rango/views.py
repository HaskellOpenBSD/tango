from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.http import HttpResponse

def index(request):
	# Request the context of the request.
	# The context contains information such as the client's machine
	# details, for example.
	context = RequestContext(request)

	# Construct a dictionary to pass to the template engine as its 
	# context.
	# Note the key boldmessage is the same as {{ boldmessage }} in
	# the template.
	context_dict = {'boldmessage': "I am bold font from the context"}

	# Return a rendered response to send to the client.
	# We make use of the shortcut function to make our lives easier.
	# Note that the firs parameter is the template we wish to use.
	return render_to_response('rango/index.html', context_dict, context)

#return HttpResponse('Rango says hello world! <br> \
#		Click <a href="/rango/about">here</a> \
#		to learn more.')

def about(request):
	return render_to_response('rango/about.html') 
#	return HttpResponse('Rango says: <br> Here is the about page. <br>\
#		Click <a href="/rango/">here</a> to go to the\
#		main page.')
