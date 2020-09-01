from django import forms


class TweetForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, max_length=140)