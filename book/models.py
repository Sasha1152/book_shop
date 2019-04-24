from django.db import models
from author.models import Author
from image.models import Image
from genre.models import Genre


class Book(models.Model):

	title = models.CharField(max_length=50)
	description = models.TextField(blank=True)
	year = models.PositiveSmallIntegerField(max_length=4)
	pages = models.PositiveSmallIntegerField(max_length=5)
	price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
	quantity = models.PositiveSmallIntegerField(max_length=2, null=True, default=1)
	author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
	image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, blank=True)
	genre = models.ManyToManyField(Genre, null=True, blank=True, related_name='genre')


	def __str__(self):
		return self.title
