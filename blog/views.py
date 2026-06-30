from django.shortcuts import render

# https://tutorial.djangogirls.org/pt/django_views/

def post_list(request):
    return render(request, 'blog/post_list.html', {})
