from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(widget=forms.TextInput(attrs={'size': '50'}))