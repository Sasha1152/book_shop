from django.db import models
from author.models import Author
from image.models import Image


class Book(models.Model):

	title = models.CharField(max_length=50)
	description = models.CharField(blank=True, max_length=1000)
	year = models.PositiveSmallIntegerField(max_length=4)
	pages = models.PositiveSmallIntegerField(max_length=5)
	price = models.PositiveSmallIntegerField(max_length=4, null=True, blank=True)
	quantity = models.PositiveSmallIntegerField(max_length=2, null=True, default=1)
	author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
	image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return self.title
