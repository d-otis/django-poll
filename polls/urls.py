from django.urls import path
from . import views

urlpatterns = [
  # empty path means it uses the path from the root URLconf
  # if changed to 'foo' for example this view can be accessed at
  # /polls/foo
  ##################################
  # /polls/
  path('', views.index, name="index"),
  # /polls/5/
  path('<int:question_id>/', views.detail, name="detail"),
  # /polls/5/results/
  path('<int:question_id>/results/', views.results, name="results"),
  # /polls/5/vote/
  path('<int:question_id>/vote/', views.vote, name="vote")
]