from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html',{})

def cover_letter(request):
    return render(request,'letter.html',{})

def gallery(request):
    return render(request,'gallery.html',{})