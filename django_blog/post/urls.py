from django.conf.urls import url
from . import views

app_name='post'

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_single, name='post_single'),
	url(r'^category/(?P<slug>.+)/$', views.category, name='category'),
	url(r'^search-results/$', views.search, name='search'),
]