from django import forms

from .models import Community, Post

class PostForm(forms.ModelForm):
    community = forms.ModelChoiceField(queryset=Community.objects.all(),empty_label=None)
    class Meta:
        model = Post
        fields = ('text', 'community')
    #content = forms.CharField(widget=forms.Textarea)
    #community = forms.ModelChoiceField(queryset=Community.objects.all(), empty_label=None)