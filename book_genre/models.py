from django.db import models
from utils.abstract_model import AbstractModel
from book.models import Book
from genre.models import Genre


class BookGenre(AbstractModel):

	book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
	genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
