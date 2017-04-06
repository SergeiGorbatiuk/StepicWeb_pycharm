from django.shortcuts import render
from qa.models import *
from django.http import HttpResponse,Http404, HttpResponseRedirect
from django.core.paginator import Paginator, InvalidPage,EmptyPage
from qa.forms import *

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def distinct_q(request, q_id):
    try:
        question = Question.objects.get(pk = q_id)
    except Question.DoesNotExist:
        raise Http404
    answers = Question.objects.get_answers(question)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(question)
            url = answer.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm(initial={'question': question.id})
    return render(request, "distinct_q.html", {"question": question, "answers": answers, "form": form})

def new_questions(request):
    page = request.GET.get('page',1)
    questions = Question.objects.new()[:]
    paginator= Paginator(questions,10)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request,"question_list.html",{
        'questions':page.object_list,
})

def popular_questions(request):
    page = request.GET.get('page',1)
    questions = Question.objects.popular()[:]
    paginator= Paginator(questions,10)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request,"question_list.html",{
        'questions':page.object_list,
})

def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()

    return render(request, "ask_add.html", {
        'form' : form
    })

