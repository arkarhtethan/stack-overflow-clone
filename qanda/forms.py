from django import forms
from .models import Question, Answer
from django.contrib.auth.models import User

class AskQuestionForm(forms.ModelForm):

    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.HiddenInput,
        disabled=True
    )

    class Meta:

        model = Question

        fields = ('title', 'question', 'user')

class AnswerForm(forms.ModelForm):

    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.HiddenInput,
        disabled=True
    )

    question = forms.ModelChoiceField(
        queryset=Question.objects.all(),
        widget=forms.HiddenInput,
        disabled=True
    )

    class Meta:

        model = Answer

        fields = ('answer', 'question', 'user')


class AnswerAcceptanceForm(forms.ModelForm):

    accepted = forms.BooleanField(
        widget=forms.HiddenInput,
        required=False
    )

    class Meta:

        model = Answer

        fields = ['accepted',]

class ContactForm(forms.Form):

    name = forms.CharField(max_length=120)

    email = forms.EmailField()

    message = forms.Textarea()
