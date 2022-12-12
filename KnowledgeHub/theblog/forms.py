from django import forms
from .models import Post,User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','category_name', 'author', 'body','header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'Write Post Title Here'}),
            'category_name': forms.Select(attrs={'class': 'form-control','placeholder':'Select The Post Category'}),
            'author': forms.TextInput(attrs={'class': 'form-control','value':'user_id','id':'user_id','type':'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control','placeholder':'Write Post Here'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'Write Post Title Here'}),
            'body': forms.Textarea(attrs={'class': 'form-control','placeholder':'Write Post Here'}),
        }

