from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from rango.models import Category, Page

def index(request):
	# Obtain the context from the HTTP request.
	context = RequestContext(request)

	context_dict = {}

	# Query for categories - add the list to our context dictionary.
	category_list = Category.objects.order_by('-likes')[:5]
	context_dict['categories'] = category_list	

	# Loop through each category returned, and create a URL attribute.
	# Stores an encoded URL (spaces replaced with underscores).
	for category in category_list:	
		category.url = category.name.replace(' ', '_')

	# Query for pages - add the list to our context dictionary.
	page_list = Page.objects.order_by('-views')[:5]
	context_dict['pages'] = page_list

	# Render the response and send it back
	return render_to_response('rango/index.html', context_dict, 
		context)

def about(request):
	return render_to_response('rango/about.html') 

def category(request, category_name_url):
	# Request our context from the request passed to us.
	context = RequestContext(request)

	# Change underscores in the category name to spaces.
	# URLs don't handle spaces well, so we encode them as underscores.	
	# We can then simply replace the underscores with spaces again to 
	# get the name.
	category_name = category_name_url.replace('_', ' ')

	# Create a context dictionary which we can pass to the template.
	# We start by containing the name of the category passed by the
	# user.
	context_dict = {'category_name': category_name}

	try:
		# Can we find a category with the given name?
		# If we can't the .get() method raises a DoesNotExist exception
		# So the method returns a model instance or raises an exception
		category = Category.objects.get(name=category_name)

		# Retrieve all of the associated pages.
		# Note that filter returns >= 1 model instance.
		pages = Page.objects.filter(category=category)

		# Adds our results to the template context under name pages.
		context_dict['pages'] = pages
		# We also add the category object from the database to the 
		# context dictionary.
		# We'll use this in the template to verify that the category 
		# exists.
		context_dict['category'] = category

	except Category.DoesNotExist:
		# We get here if we din't find the specified category.
		# Do nothing -- the template displays the 'no category'.
		pass

	return render_to_response('rango/category.html', context_dict, 
		context)
