from django import forms

from .models import candidate


class PostForm(forms.ModelForm):
    class Meta:
        model = candidate
        fields = ('name', 'planet', 'age', 'email')


class SaveAnswer(forms.ModelForm):
    class Meta:
        model = candidate
        fields = ('answers',)
