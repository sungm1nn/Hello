from django import forms
from .models import user_subs
 
class CreateBlog(forms.ModelForm):
    class Meta:
        model = user_subs()
        fields = ['title', 'pub_date', 'body']