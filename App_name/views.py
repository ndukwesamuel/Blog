from django.shortcuts import render, redirect

# Create your views here.
from .models import BlogPost


def home(request):
    data = BlogPost.objects.all()

    context = {
        'data_key': data
    }

    return render(request, 'index.html', context)


def details(request, pk):
    print(type(pk))
    data = BlogPost.objects.get(id=pk)

    context = {
        'data_key': data
    }

    return render(request, 'details.html', context)

def DeleteView(request, pk):
    data = BlogPost.objects.get(id=pk)
    data.delete()
    return redirect('home')
