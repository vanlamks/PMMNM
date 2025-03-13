from django.shortcuts import render

# Create your views here.
def get_name(request):
    return render(request, 'home.html')
    