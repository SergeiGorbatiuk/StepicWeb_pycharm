from django import forms
from qa.models import *
from django.contrib.auth import authenticate

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget = forms.Textarea)
    #author = forms.CharField(widget=forms.HiddenInput())

    def clean(self):
        pass

    def save(self):
        self.cleaned_data['author'] = self.author
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
        self.cleaned_data['author'] = self.author
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer

class SignupForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def save(self):
        user = User.objects.create_user(**self.cleaned_data)
        user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def save(self):
        user = authenticate(**self.cleaned_data)
        return user