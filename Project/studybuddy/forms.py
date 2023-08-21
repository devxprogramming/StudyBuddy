from django import forms
from django.forms import ModelForm

from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control', "rows":'3', "cols":'3', 'placeholder':'This is the Description for the Room to be created...'}),
            'host':forms.Select(attrs={'class':'form-select'}),
            'topic':forms.Select(attrs={'class':'form-select'}),
        }