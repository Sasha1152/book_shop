from django.db import models
from book.models import Book
from order.models import Order

class Suborder(models.Model):

	id = models.AutoField(primary_key=True)
	quantity = models.PositiveSmallIntegerField(max_length=2)
	is_returned = models.BooleanField()
	order_date = models.DateField()
	book_id = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
	order_id = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return str(self.id)