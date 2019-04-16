from django.db import models
from utils.abstract_model import AbstractModel
from book.models import Book
from order.models import Order

class Suborder(AbstractModel):

	quantity = models.PositiveSmallIntegerField(max_length=2)
	is_returned = models.BooleanField()
	order_date = models.DateField()
	book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
	order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
