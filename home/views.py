# Create your views here.
from django.http import HttpResponse
from upload.models import Track
from django.shortcuts import render

def index(request):
    query = request.GET.get('search', '')
    tracks = Track.objects.all()

    if query:
        tracks = tracks.filter(title__icontains=query)

    context = {
        'tracks': tracks,
        'query': query
    }
    return render(request, 'home/index.html', context)