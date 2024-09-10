from django import forms

class CreateTask(forms.Form):
    name = forms.CharField(label= "Tarea",max_length=30)
    description = forms.CharField(widget=forms.Textarea)
    date_end = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), 
        label='Fecha de entrega')
class UpdateTask(forms.Form):
    name = forms.CharField(label= "Tarea",max_length=30, initial= "")
    description = forms.CharField(widget=forms.Textarea)
    date_end = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), 
        label='Fecha de entrega')
    task_id = forms.IntegerField()

class DeleteTask(forms.Form):
    task_id = forms.IntegerField()