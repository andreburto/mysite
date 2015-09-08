from django.http import HttpResponse
from django.template.defaulttags import csrf_token
from django.shortcuts import render, redirect
from models import People
import Hello

def index(request):
    Hello.hi()
    context_dict = {'title': "Home", 'msg': "Andy's Django Project", 'img': "bulbasaur.jpg"}
    return render(request, 'index.html', context_dict)

def about(request):
    context_dict = {'title': "About", 'msg': 'This is the about page.'}
    return render(request, 'about.html', context_dict)

def names(request):
    names = ""
    for p in People.objects.all():
        names += "<p>"+p.name+"</p>"
    context_dict = {'title': "Names", 'msg': names}
    return render(request, 'about.html', context_dict)

def names_add(request):
    if request.method == 'GET':
        phtml = "<input type=\"text\" name=\"name\" value=\"\" /><input type=\"submit\" />"
        context_dict = {'title':"Who are you?",'msg':phtml,'action':"/names/add"}
        return render(request, 'form.html', context_dict)
    elif request.method == 'POST':
    	new_person = People(name=request.POST['name'])
    	new_person.save()
    	return redirect('names')
    else:
        context_dict = {'title': "ERROR", 'msg':"Not a valid method."}
        return render(request, 'form.html', context_dict)

def form(request):
    context_dict = ""
    html = ""
    if request.method == 'GET':
        phtml = "<input type=\"text\" name=\"name\" value=\"\" /><input type=\"submit\" />"
        context_dict = {'title':"Who are you?",'msg':phtml,'action':"/form"}
    elif request.method == 'POST':
        phtml = "Hello, "+request.POST['name']+"!"
        context_dict = {'title':"Hello",'msg':phtml}
    else:
        context_dict = {'title': "ERROR", 'msg':"Not a valid method."}
    return render(request, 'form.html', context_dict)
