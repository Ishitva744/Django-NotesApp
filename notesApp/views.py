from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import notes
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.

def home(request):
	return render(request, 'home.html')
	
	
def mynotes(request):
	user = request.user
	title = notes.objects.filter(user = user)
	context= {
		'note': title,
		}
	return render(request , "mynotes.html" , context)

def create(request):
	if request.method == 'POST':
		title = request.POST['title']
		text = request.POST['text']

		note = notes(user = request.user, title = title , text = text)
		note.save()

		
		messages.success(request, "New Note Created.")
		return redirect('create')
	
	return render(request, 'create.html')


def delete(request, id):
	note = notes.objects.get(id=id)
	note.delete()
	messages.info(request, "Note Deleted!")
	return redirect('mynotes')



def update(request, id):	
	if request.method == "POST":
		title = request.POST['title']
		text = request.POST['text']
		note = notes.objects.get(id=id)
		note.title = title
		note.text = text
		note.save()
		messages.info(request, "Note updated.")
		return redirect('mynotes')
		
	else:	
		note = notes.objects.get(id=id)
		template = loader.get_template('update.html')
		context = {
				'item' : note
		}
		return HttpResponse(template.render(context, request))
