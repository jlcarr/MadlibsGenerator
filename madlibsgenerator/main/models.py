from django.db import models

class BaseText(models.Model):
	text = models.CharField(max_length=600)
	creation_date = models.DateTimeField('creation date', auto_now_add=True)
	def __str__(self):
		return self.text[:10]

class Substitution(models.Model):
	base_text = models.ForeignKey(BaseText, on_delete=models.CASCADE)
	swap_id = models.IntegerField()
	pos = models.CharField(max_length=10)
	tag = models.CharField(max_length=10)
	def __str__(self):
		return f"({self.swap_id}: {self.pos}-{self.tag})"
