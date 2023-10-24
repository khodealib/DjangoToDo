from django import forms

from home.models import Todo


class TodoCreateForm(forms.Form):
    title = forms.CharField(max_length=255)
    body = forms.CharField(widget=forms.Textarea)
    created = forms.DateTimeField(widget=forms.DateTimeInput)


class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ("title", "body", "created")
