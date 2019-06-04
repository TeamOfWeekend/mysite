from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Topic(models.Model):
	"""用户学习的主题"""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(
		User, 	# 这里应该是 User, 而不是 'User', 否则会报错
		on_delete=models.CASCADE,
	)
	
	def __str__(self):
		"""返回模型的字符串表示"""
		return self.text
		
		
# Entry
class Entry(models.Model):
	"""学到的有关某个主题的具体知识"""
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE,)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		verbose_name_plural = 'entries'
		
	def __str__(self):
		"""返回模型的字符串表示"""
		return self.text[:50] + "..."
