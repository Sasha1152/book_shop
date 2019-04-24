from django.db import models
from user.models import User

class Order(models.Model):

	id = models.AutoField(primary_key=True)
	total_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
	is_returned = models.BooleanField()
	user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return str(self.id)
