from django import forms
from music.models import Playlist

class SearchForm(forms.Form):
    search_flag = forms.BooleanField(widget=forms.HiddenInput(), initial=True, required=False)
    query = forms.CharField(widget=forms.TextInput(attrs={'size': '30', 'style' : 'border-radius: 8px; border-width: 1px; border-color: black; margin-left: 10px; color:  #636261; padding: 5px;'}))
    
    
class ListForm(forms.Form):
    Playlist = forms.ModelChoiceField(queryset=Playlist.objects.all(),empty_label=None)

class AddPlayListForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'size': '30', 'style' : 'border-radius: 8px; border-width: 1px; border-color: black; margin-left: 10px; color:  #636261; padding: 5px;'}))
   