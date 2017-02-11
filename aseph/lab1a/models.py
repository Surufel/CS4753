# Sifer Aseph

from __future__ import unicode_literals

# For validation:
import os
from django.core.exceptions import ValidationError

from django.db import models
from django.utils import timezone

# https://docs.djangoproject.com/en/1.10/ref/validators/
def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.gif', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Only [jpg, gif, png] allowed.')

class Image(models.Model):
    """For reference: https://docs.djangoproject.com/en/1.10/ref/models/fields/

    ImageForm inherits from Django's Model. Images class will be generated this way.
    """
    image_file = models.FileField(upload_to='pictures', verbose_name="Image", validators=[validate_file_extension]) # Default is class name.
    #caption = models.CharField(max_length=100)

    date = models.DateTimeField(default=timezone.now)
