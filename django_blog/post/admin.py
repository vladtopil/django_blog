from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'date_created', 'is_moderated')

class CommentAdmin(admin.ModelAdmin):
	list_display = ('id', 'post', 'text', 'date_created', 'is_moderated')

admin.site.register(Post, PostAdmin)
admin.site.register(CommentPost, CommentAdmin)
admin.site.register(Category)

