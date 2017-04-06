from django import forms
from qa.models import *

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget = forms.Textarea)

    def clean(self):
        pass

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput())

    def clean(self):
        pass

    def save(self, question):
        self.cleaned_data['question'] = question
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer