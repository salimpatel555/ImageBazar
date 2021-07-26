from django import forms
from django.db import models
from django.db.models import fields
from .models import*


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        labels = {'cat':'Category'}
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control',}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'added_date':forms.SelectDateWidget(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'})

        }
        


        