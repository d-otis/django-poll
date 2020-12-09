from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# originally needed this in the OG index()
# from django.template import loader

from .models import Choice, Question
# Create your views here.

def index(request):
  # original example
  # return HttpResponse("Hello, world. You're @ the polls index!")
  # ORIGINAL w/ Template
  # latest_question_list = Question.objects.order_by('-pub_date')[:5]
  # template = loader.get_template('polls/index.html')
  # context = {
  #   'latest_question_list': latest_question_list
  # }
  # return HttpResponse(template.render(context, request))
  # REWRITTEN 
  # since this is such a common pattern
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  context = {'latest_question_list': latest_question_list}
  return render(request, 'polls/index.html', context)


def detail(request, question_id):
  # OG Stub
  # return HttpResponse("You're looking @ question %s." % question_id)
  # ###############################
  # VERBOSE TRY/EXCEPT for querying DB
  # try:
  #   question = Question.objects.get(pk=question_id)
  # except Question.DoesNotExist:
  #   raise Http404("Question does not exist")
  # return render(request, 'polls/detail.html', {'question': question})
  # ###############################
  # REFACTORED to auto raise 404 exception when needed
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
  response = "You're looking @ the results for question %s."
  return HttpResponse(response % question_id)

def vote(request, question_id):
  return HttpResponse("You're voting on question %s." % question_id)