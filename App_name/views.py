from django.shortcuts import render, redirect

# Create your views here.
from .models import BlogPost
from .forms import BlogForm



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


def CreateView(request):
    form_data = BlogForm(request.POST or None)
    if form_data.is_valid():
        form_data.save()
        return redirect('home')
    else:
        print('bad code')


    return render(request, 'create.html')

def UpdateView(request, pk):
    data = BlogPost.objects.get(id=pk)
    form_data = BlogForm(request.POST or None, instance=data )
    if form_data.is_valid():
        form_data.save()
        return redirect('home')
    else:
        print('bad code')

    context = {
        'form_data': form_data,
        'data':data
    }

    return render(request, 'update.html', context)