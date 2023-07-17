from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import movie
from . forms import movieform
# Create your views here.
def index(request):
    movieinfo = movie.objects.all()
    context ={
        'movie_list':movieinfo
    }
    return render(request,'index.html',context)
def detail(request,movie_id):
    moviedet=movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'moviedet_key':moviedet})
def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        image=request.FILES['image']
        new_movie=movie(name=name,desc=desc,year=year,image=image)
        new_movie.save()
        return redirect('/')
    return render(request,'add.html')

def update(request, id):
    movieupdate=movie.objects.get(id=id)
    form=movieform(request.POST or None, request.FILES,instance=movieupdate)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html',{'form_key':form,'movieupdate_key':movieupdate})
def delete(request,id):
    if request.method=='POST':
        moviedel=movie.objects.get(id=id)
        moviedel.delete()
        return redirect('/')
    return render(request,'delete.html')