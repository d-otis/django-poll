from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Question
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
  return HttpResponse("You're looking @ question %s." % question_id)

def results(request, question_id):
  response = "You're looking @ the results for question %s."
  return HttpResponse(response % question_id)

def vote(request, question_id):
  return HttpResponse("You're voting on question %s." % question_id)