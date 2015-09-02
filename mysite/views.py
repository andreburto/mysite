from django.http import HttpResponse
from django.template.defaulttags import csrf_token
from django.shortcuts import render
from models import People
from parity import Parity

def index(request):
    context_dict = {'title': "Home", 'msg': "Andy's Django Project", 'img': "bulbasaur.jpg"}
    return render(request, 'index.html', context_dict)

def about(request):
    context_dict = {'title': "About", 'msg': 'This is the about page.'}
    return render(request, 'about.html', context_dict)

def names(request):
    names = ""
    for p in People.objects.all()[:5]:
        names += "<p>"+p.name+"</p>"
    context_dict = {'title': "Names", 'msg': names}
    return render(request, 'about.html', context_dict)

#@csrf_token
def form(request):
	context_dict = ""
	phtml = ""
	if request.method == 'GET':
		phtml = "<input type=\"text\" name=\"name\" value=\"\" /><input type=\"submit\" />"
		context_dict = {'title':"Who are you?",'msg':phtml}
	elif request.method == 'POST':
		phtml = "Hello, "+request.POST['name']+"!"
		context_dict = {'title':"Hello",'msg':phtml}
	else:
		context_dict = {'title': "ERROR", 'msg':"Not a valid method."}
	return render(request, 'form.html', context_dict)
