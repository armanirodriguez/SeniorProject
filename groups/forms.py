from django import forms

from .models import Community, Post

class PostForm(forms.ModelForm):
    community = forms.ModelChoiceField(queryset=Community.objects.all(),empty_label=None)
    class Meta:
        model = Post
        fields = ('text', 'community')
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'myfieldclass'})
    #content = forms.CharField(widget=forms.Textarea)
    #community = forms.ModelChoiceField(queryset=Community.objects.all(), empty_label=None)