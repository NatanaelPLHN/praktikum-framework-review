from django import forms
from .models.students import Students  # Import the Students class directly

class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students  # Use the class name here
        fields = '__all__'
