from django import forms
from .models import BlogPost
from users.models import Bio

class PostForm(forms.ModelForm):
    """form for adding a post"""
    title=forms.CharField()
    text=forms.CharField(widget=forms.Textarea(attrs={'cols': 60}))
    class Meta:
        model=BlogPost
        fields=['title','text']
        label={'text':''}
        #widgets = {'text': forms.Textarea(attrs={'cols': 85})}

class BioForm(forms.ModelForm):
    """form for user biography"""
    text=forms.CharField(widget=forms.Textarea(attrs={'cols':60}))
    class Meta:
        model=Bio
        fields=['text']
        label={'text': ''}