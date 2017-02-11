# Sifer Aseph

from django import forms

from django.forms import ModelForm
from django.forms import formset_factory

from .models import Image

class ImageForm(forms.ModelForm):
    """For reference: https://docs.djangoproject.com/en/1.10/ref/forms/fields/

    ImageForm inherits from Django's Form. ImageForm class will be generated this way.
    """
    #image_file = forms.FileField(label='Pick an image.')
    #caption = forms.CharField(label='Write something.')
    class Meta:
        model = Image
        fields = ['image_file']

ImageFormset = forms.formset_factory(ImageForm, extra = 1)
