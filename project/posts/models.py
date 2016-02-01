from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Post(models.Model):
	brand = models.CharField(max_length = 50)
	brand_type = models.CharField(max_length = 80)
	description = models.TextField()
	price = models.DecimalField(max_digits = 6, decimal_places = 2)

	def __str__(self):
		return self.brand
		# return "{} {}".format(self.brand, self.brand_type)

	# def get_absolute_url(self):
	# 	print()
	# 	return reverse("posts:detail", kwargs={"id":self.id})