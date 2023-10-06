from django.shortcuts import redirect, render, get_object_or_404
from .models import Movie
from .forms import MovieForm
from django.views.decorators.http import require_POST, require_http_methods, require_safe
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies,
    }
    return render(request,'movies/index.html',context)

@login_required
def create(request):
    if request.method=='POST':
        form = MovieForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('movies:index')
    
    else:
        form = MovieForm()

    context = {
        'form' : form,
    }
    return render(request,'movies/create.html',context)
@login_required
def detail(request,pk):
    movie = get_object_or_404(Movie,pk=pk)
    context = {
        'movie' : movie,
    }
    return render(request,'movies/detail.html',context)
@login_required
def update(request,pk):
    movie = get_object_or_404(Movie,pk=pk)
    if request.method=='POST':
        form = MovieForm(request.POST,request.FILES, instance=movie)
        if form.is_valid():
            form.save()
        return redirect('movies:detail',movie.pk)
    
    else:
        form = MovieForm(instance=movie)

    context = {
        'form' : form,
        'movie' : movie,
    }
    return render(request,'movies/update.html',context)

def delete(request,pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')