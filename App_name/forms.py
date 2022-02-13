from django import forms


from .models import BlogPost


class BlogForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = BlogPost
        fields = "__all__"