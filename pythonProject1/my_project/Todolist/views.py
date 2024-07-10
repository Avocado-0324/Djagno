# views.py
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo, SubTodo
from .forms import TodoForm, SubTodoForm


def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo_list.html', {'todos': todos})


def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'add_todo.html', {'form': form})


def edit_todo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    SubTodoFormSet = inlineformset_factory(Todo, SubTodo, form=SubTodoForm, extra=1)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        formset = SubTodoFormSet(request.POST, instance=todo)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
        formset = SubTodoFormSet(instance=todo)

    return render(request, 'edit_todo.html', {'form': form, 'formset': formset})


def delete_todo(request, todo_id):
    if request.method == 'POST':
        todo = get_object_or_404(Todo, pk=todo_id)
        checkbox_id = request.POST.get('delete-checkbox')
        if checkbox_id and request.POST.get(checkbox_id) == 'on':
            todo.delete()
    return redirect('todo_list')
