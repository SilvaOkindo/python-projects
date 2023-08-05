#from django.views.generic import TemplateView


from django.shortcuts import render
from . models import Post

# Create your views here.

# class Hello(TemplateView):
#     template_name = "home.html"
    
    
# class AboutPage(TemplateView):
#     template_name = "about.html"


def post_list(request):
    posts = Post.objects.all()
    return render(
        request,
        'templates/blog/home.html',
        {'posts': posts}
    )