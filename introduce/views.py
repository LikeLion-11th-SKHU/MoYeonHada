from django.shortcuts import render

# Create your views here.
def introduce_main(request):
    return render(request, 'introduce_main.html')

def introduce_developer(request):
    return render(request, 'introduce_developer.html')