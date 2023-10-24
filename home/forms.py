from django import forms


class TodoCreateForm(forms.Form):
    title = forms.CharField(max_length=255)
    body = forms.CharField()
    created = forms.DateTimeField()
