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

    def __init__(self, *args, **kwargs):
        task_instance = kwargs.pop("instance", None)
        super().__init__(*args, **kwargs)
        if task_instance:
            self.fields["name"].initial = task_instance.name
            self.fields["description"].initial = task_instance.description
            self.fields["date_end"].initial = task_instance.date_end

class DeleteTask(forms.Form):
    task_id = forms.IntegerField()