from django.shortcuts import render

# Create your views here.
def posts_list(request):
    return render(request, 'posts_list.html')
    