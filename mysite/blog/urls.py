from django.urls import path
from . import views



urlpatterns = [
    path("", views.post_list, name='posts'),
    #path("", Hello.as_view(), name='home')
]

