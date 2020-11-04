from django.db import models
import uuid                 

class VideoJuego(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	name = models.CharField(max_length=200)
	departure = models.DateField(null=True, blank=True)
	price = models.IntegerField

	def __str__(self):
		return f'{self.id}, {self.name}, {self.departure}, {self.price}'
	 