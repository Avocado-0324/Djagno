from django import forms
from .models import Todo, SubTodo


class DateInput(forms.DateInput):
    input_type = 'date'


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'due_date', 'priority']
        widgets = {
            'due_date': DateInput(),
        }


class SubTodoForm(forms.ModelForm):
    class Meta:
        model = SubTodo
        fields = ['title', 'completed']
