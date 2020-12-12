from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

# originally needed this in the OG index()
# from django.template import loader

from .models import Choice, Question
# Create your views here.

def IndexView(generic.ListView):
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
  # latest_question_list = Question.objects.order_by('-pub_date')[:5]
  # context = {'latest_question_list': latest_question_list}
  # return render(request, 'polls/index.html', context)
  # #############################
  # REFACTORED FOR GENERIC VIEWS
  template_name = 'polls/index.html'
  context_object_name = 'latest_question_list'

  def get_queryset(self):
    """ Return the last five published questions. """
    return Question.objects.order_by('-pub_date')[:5]


def detail(generic.DetailView):
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
  # question = get_object_or_404(Question, pk=question_id)
  # return render(request, 'polls/detail.html', {'question': question})
  #   # ###############################
  # REFACTORED FOR GENERIC VIEWS
  model = Question
  template_name = 'polls/detail.html'

def results(generic.DetailView):
  # question = get_object_or_404(Question, pk=question_id)
  # return render(request, 'polls/results.html', {'question': question})
  #   # ###############################
  # REFACTORED FOR GENERIC VIEWS
  model = Question
  template_name = 'polls/results.html'

def vote(request, question_id):
  # OG Stub-out
  # return HttpResponse("You're voting on question %s." % question_id)
  question = get_object_or_404(Question, pk=question_id)
  try:
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    # Redisplay the question voting form.
    return render(request, 'polls/detail.html', {
      'question': question,
      'error_message': "You didn't select a choice!"
    })    
  else:
    selected_choice.votes += 1
    selected_choice.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    
    # reverse() is similar to url template tag in .html files
    # that's why referencing the polls/results route looks like:
    # 'polls:results' -- if we just had one app, the polls one:
    # we could just use 'results' as the first argument
    # the args is the pk that the path('<int:question_id/results/') needs to
    # query the results