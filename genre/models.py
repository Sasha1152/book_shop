from django.db import models
# from book.models import Book


class Genre(models.Model):
	name = models.CharField(max_length=64, blank=True)
	# book = models.ManyToManyField(Book)

	def __str__(self):
		return self.name