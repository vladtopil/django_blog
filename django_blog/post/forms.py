from .models import CommentPost
from django import forms

class CommentForm(forms.ModelForm):
	class Meta():
		model = CommentPost
		fields = ('text',)