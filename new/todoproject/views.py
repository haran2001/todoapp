from django.shortcuts import render
from .models import toDoListItem
from django.http import HttpResponseRedirect

def toDoAppView(request):
	all_todo_items = toDoListItem.objects.all()
	context  = {'all_items':all_todo_items}
	return render(request, 'todolist.html', context)

def homeView(request):
	return render(request, 'home.html')

def page1View(request):
	return render(request, 'page1.html')

def addToDoView(request):
	x = request.POST['content']
	new_item = toDoListItem(content = x)
	new_item.save()
	return HttpResponseRedirect('/todoapp')

def deleteToDoView(request, i):
	y = toDoListItem.objects.get(id = i)
	y.delete()
	return HttpResponseRedirect('/todoapp')