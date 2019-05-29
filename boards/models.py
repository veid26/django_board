from django.db import models
import math
from django.utils.text import Truncator
# Create your models here.

class Board(models.Model):
	name = models.CharField(max_length=30, unique=True)
	description = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Topic(models.Model):
	subject = models.CharField(max_length=2500)
	last_updated = models.DateTimeField(auto_now_add=True)
	board = models.ForeignKey(Board, related_name='topics', on_delete=True)
	views = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.subject

	def get_page_count(self):
		count = self.posts.count()
		pages = count / 20
		return math.ceil(pages)
	def has_many_pages(self, count=None):
		if count is None:
			count = self.get_page_count()
		return count > 6
	def get_page_range(self):
		count = self.get_page_count()
		if self.has_many_pages(count):
			return range(1, 5)
		return range(1, count + 1)
	def get_last_ten_posts(self):
		return self.posts.order_by('-created_at')[:10]

class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)