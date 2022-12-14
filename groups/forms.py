from django import forms

from .models import Community, Post, Comment

class PostForm(forms.ModelForm):
    post_flag = forms.BooleanField(widget=forms.HiddenInput(), initial=True)
    community = forms.ModelChoiceField(queryset=Community.objects.all(),empty_label=None)
    class Meta:
        model = Post
        fields = ('text', 'community')
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.label_suffix = "" 
        self.fields['text'].widget.attrs.update({'style': 'border-radius: 8px; border-color: black; margin-left: 10px; padding: 5px; border-width: 1px;'})
        self.fields['community'].widget.attrs.update({'style': 'border-radius: 8px; border-color: black; margin-left: 10px; padding: 5px;'})
    #content = forms.CharField(widget=forms.Textarea)
    #community = forms.ModelChoiceField(queryset=Community.objects.all(), empty_label=None)

class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea, label='')
    class Meta:
        model = Comment
        fields = ('body',)
class createCommunityForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={ 'style' : 'border-radius: 8px; border-width: 1px; border-color: black; color:  #636261; padding: 5px;'}))
