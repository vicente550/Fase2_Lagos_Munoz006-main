from django.shortcuts import render
from . models import VideoJuego
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.
def index(request):
    num_VideoJuego= VideoJuego.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_VideoJuego': num_VideoJuego},
    )

class VideoJuegoCreate(CreateView):
    model = VideoJuego
    fields = '__all__'
    initial ={'departure': '19/11/2020'}

class VideoJuegoUpdate(UpdateView):
    model = VideoJuego
    fields = ['id', 'name', 'departure', 'price']

class VideoJuegoDelete(DeleteView):
    model = VideoJuego
    success_url = reverse_lazy('videojuego')

class VideoJuegoDetailView(generic.DetailView):
    model = VideoJuego

class VideojuegoListView(generic.ListView):
    model = VideoJuego

