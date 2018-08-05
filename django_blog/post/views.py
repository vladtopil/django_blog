from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .forms import CommentForm
from .models import *


def post_list(request):
	posts = Post.objects.filter(is_moderated=True, date_created__lte=datetime.now()).order_by('-date_created')
	categories = Category.objects.exclude(pk=1)

	return render(request, 'index.html', {'posts': posts, 'categories': categories})

def post_single(request, pk):
	post = get_object_or_404(Post, pk=pk)
	comment = CommentPost.objects.filter(post=post, is_moderated=True)
	categories = Category.objects.exclude(pk=1)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comm = form.save(commit=False)
			comm.user = request.user
			comm.post = post
			comm.save()
			form = CommentForm()

	else:		
		form = CommentForm()
	return render(request, "post.html", { 'post': post, 'form': form, 'comment': comment, 'categories': categories})

def category(request, slug):
	category = get_object_or_404(Category,slug=slug)
	categories = Category.objects.exclude(pk=1)
	posts = category.entries.order_by('-date_created')

	return render(request, "cat.html", {'category': category, 'categories': categories, 'posts': posts})

def search(request):
	query = request.GET.get('q') or ''
	posts = Post.objects.filter(title__icontains=query).order_by('-date_created')
	categories = Category.objects.exclude(pk=1)

	return render(request, "search-results.html", {'categories': categories, 'posts': posts, 'query': query})