from django import forms

class SearchForm(forms.Form):
    search_flag = forms.BooleanField(widget=forms.HiddenInput(), initial=True)
    query = forms.CharField(widget=forms.TextInput(attrs={'size': '30'}))