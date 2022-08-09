
from cProfile import label
from django import forms
from .models import image

class photoload(forms.ModelForm):
    class Meta:
        model=image
        fields= '__all__'
        labels={'photo':''}