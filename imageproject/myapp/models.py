# -*- coding: utf-8 -*-
from django.db import models

class image(models.Model):
    imagefile = models.ImageField(upload_to='images/%Y/%m/%d')
    caption = models.CharField(max_length=100)
    short_desc = models.CharField(max_length=200)
    favourite = models.BooleanField(default=False)