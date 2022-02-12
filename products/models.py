from distutils.command.upload import upload
from email.policy import default
from django.db import models
from users.models import Profile

# Create your models here.
class Product(models.Model):
	salesman = models.ForeignKey(Profile, verbose_name="Salesman", on_delete=models.CASCADE)
	title = models.CharField("Item name", max_length=255)
	image = models.ImageField("Image", blank=True, default="media/IMG_20220129_201111_236-01-01.jpeg")
	describe = models.CharField("Short describe", max_length=255)
	price = models.PositiveIntegerField("Price", default=0)
	is_publish = models.BooleanField("Show in shop", default=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Product"
		verbose_name_plural = "Products"