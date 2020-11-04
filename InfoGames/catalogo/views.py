from django.shortcuts import render
from .models import VideoJuego
# Create your views here.
def index(request):
    num_VideoJuego= VideoJuego.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_VideoJuego': num_VideoJuego},
    )