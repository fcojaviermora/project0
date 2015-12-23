'''
Created on 16 de dic. de 2015

@author: fjmora
'''
from django import forms

class RecipeImagesForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
    )
    