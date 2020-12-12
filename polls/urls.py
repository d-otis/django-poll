from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
  # empty path means it uses the path from the root URLconf
  # if changed to 'foo' for example this view can be accessed at
  # /polls/foo
  ##################################
  # /polls/
  path('', views.IndexView.as_view(), name="index"),
  # /polls/5/
  # the 'name' value as called by the {% url %} template tag
  path('<int:pk>/', views.DetailView.as_view(), name="detail"),
  # /polls/5/results/
  path('<int:pk>/results/', views.ResultsView.as_view(), name="results"),
  # /polls/5/vote/
  path('<int:question_id>/vote/', views.vote, name="vote")
]