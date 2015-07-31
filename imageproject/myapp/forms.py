# -*- coding: utf-8 -*-
from django import forms

class imageForm(forms.Form):
    imagefile = forms.ImageField(
        label='Select a file'
    )
    caption = forms.CharField(
        label='Caption'
    )
    short_desc = forms.CharField(
        label='Description'
    )
