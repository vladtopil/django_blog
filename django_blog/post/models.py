from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	'''Модель статей'''
	class Meta():
		db_table = 'post'
		verbose_name = 'Статья'
		verbose_name_plural = 'Статьи'
		ordering = ['date_created']

	title = models.CharField('Заголовок', max_length=100)
	category = models.ForeignKey('Category', related_name='entries', default=1)
	text = models.TextField('Текст статьи', max_length=1500)
	image = models.ImageField('Изображение', upload_to='post/', blank=True)
	date_created = models.DateTimeField('Создан', auto_now_add=True)
	date_updated = models.DateTimeField('Обновлено', auto_now=True)
	is_moderated = models.BooleanField('Модерация', default=False)

	def __str__(self):
		return self.title

class CommentPost(models.Model):
	'''Модель комментариев'''
	class Meta():
		db_table = 'comments'
		verbose_name = 'Комментарии'
		verbose_name_plural = 'Комментарии'

	user = models.ForeignKey(User, verbose_name = 'Пользователь')
	post = models.ForeignKey(Post, verbose_name = 'Статья')
	text = models.TextField('Текст комментария')
	date_created = models.DateTimeField('Добавлен', auto_now_add=True)
	is_moderated = models.BooleanField('Модерация', default=False)

	def __str__(self):
		return self.text

class Category(models.Model):
	''' Модель категории '''
	class Meta():
		db_table = 'category'
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

	title = models.CharField('Название', max_length=100)
	slug = models.SlugField('Slug')

	def __str__(self):
		return self.title

	




