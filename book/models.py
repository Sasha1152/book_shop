from django.db import models
from utils.abstract_model import AbstractModel
from author.models import Author
from image.models import Image


class Book(AbstractModel):

	title = models.CharField(max_length=50)
	year = models.PositiveSmallIntegerField(max_length=4)
	pages = models.PositiveSmallIntegerField(max_length=5)
	description = models.CharField(blank=True, max_length=1000)
	quantity = models.PositiveSmallIntegerField(max_length=2, default=1)
	author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
	image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)


	def __str__(self):
		return self.title
