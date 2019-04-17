from django.db import models

class Image(models.Model):

	image = models.ImageField(blank=True, upload_to='image/images/')
