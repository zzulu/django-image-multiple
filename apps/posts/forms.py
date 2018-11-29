from django import forms
from .models import Post, Image
from django.forms import inlineformset_factory


class ImageForm(forms.ModelForm):
    file = forms.ImageField()

    class Meta:
        model = Image
        fields = ['file',]


ImageFormSet = inlineformset_factory(Post, Image, form=ImageForm, extra=3)
