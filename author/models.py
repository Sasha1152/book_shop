from django.db import models
from image.models import Image


class Author(models.Model):
	first_name = models.CharField(max_length=64, blank=True)
	last_name = models.CharField(max_length=64, blank=True)
	biography = models.TextField()
	image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return self.last_name