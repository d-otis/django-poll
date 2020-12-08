from django.urls import path
from . import views

urlpatterns = [
  # empty path means it uses the path from the root URLconf
  # if changed to 'foo' for example this view can be accessed at
  # /polls/foo
  path('', views.index, name="index")
]