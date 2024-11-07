from django.shortcuts import render, redirect, get_object_or_404
from .forms import toDolistsForm
from .models import toDolists


# Create your views here.
def todo_list(request):
     todos = toDolists
     return render(request, "home.html")


def todo_list_create(request):
     if request.method=='Post':
          form = toDolistsForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('todo_list')
     else:
          form = toDolistsForm() # Create empty form instance for Get requests
     return redirect('todo_list')


def todo_list_update(request,pk):
     todo=get_object_or_404(toDolists,pk=pk)
     if request.method=='POST':
          form=toDolistsForm(request.POST, instance=todo)
          if form.is_valid():
               form.save()
               return redirect("todo_list")
     else:
          form=toDolists(instance=todo)
     return redirect('todo_list')


def todo_list_delete(request,pk):
     todo=get_object_or_404(toDolists,pk=pk)
     if request.method=="POST":
          todo.delete()
     return redirect('todo_list')


def todo_list_read(pk):
     todo = get_object_or_404(toDolists,pk=pk)
     
     print(f"/t/t{todo.title}\n")
     print(f"Description: {todo.description}\n")
     print(f"Task: {todo.description}\n")

     return redirect('todo_list')
