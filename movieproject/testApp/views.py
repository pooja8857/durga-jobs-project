from django.shortcuts import render
from .models import Movie
from . import forms

# Create your views here.
def indexview(request):
    return render(request,'testApp/index.html')


def addmovie(request):
    form = forms.MovieForm()
    if request.method == 'POST':
        form = forms.MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print('form data inserted into Database Successfully')
            return indexview(request)
    return render(request,'testApp/addmovie.html',context={'form':form})
    
def listofmovies(request):
    movie_list = Movie.objects.all()
    return render(request,'testApp/listofmovies.html',context={'movie_list':movie_list})
    
    
    
    