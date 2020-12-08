from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
  return HttpResponse("Hello, world. You're @ the polls index!")

def detail(request, question_id):
  return HttpResponse("You're looking @ question %s." % question_id)

def results(request, question_id):
  response = "You're looking @ the results for question %s." % question_id
  return HttpResponse(response % question_id)

def vote(request, question_id):
  return HttpResponse("You're voting on question %s." % question_id)