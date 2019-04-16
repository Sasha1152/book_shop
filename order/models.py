from django.db import models
from utils.abstract_model import AbstractModel
from user.models import User

class Order(AbstractModel):

	total_price = models.DecimalField(max_digits=6, decimal_places=2)
	is_returned = models.BooleanField()
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
