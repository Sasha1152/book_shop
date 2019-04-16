from django.db import models


class AbstractModel(models.Model):

	class Meta:
		abstract = True

	@classmethod
	def get_by_id(cls, obj_id):
		return cls.objects.get(id=obj_id)

	@classmethod
	def delete_by_id(cls, obj_id):
		obj = cls.objects.get(id=obj_id)
		obj.delete()
		return True

	@classmethod
	def create(cls, **kwargs):
		cls.objects.create(kwargs)
		return True


	def update(self, **kwargs):
		update_fields = []
		for key, value in kwargs.items():
			if value:
				setattr(self, key, value)
				update_fields.append(key)
			self.save(update_fields=update_fields)
		return True
