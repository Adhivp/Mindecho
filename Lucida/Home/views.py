from django.shortcuts import *

# Create your views here.
def intro(request):
    if request.method == 'POST' and 'button_pressed' in request.POST:
        return redirect('home')
    return render(request,'intro.html')

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')