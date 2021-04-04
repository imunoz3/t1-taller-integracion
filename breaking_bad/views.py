from django.shortcuts import render
from django.http import HttpResponse
import requests


# Create your views here.
def home(request):
    return render(request, 'Home.html')

def temporadas(request, serie):
    response = requests.get(f'https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series={serie}').json()
    temporadas = {}
    numero_temporadas = int(response[len(response)-1]['season'])
    for i in range(numero_temporadas):
        temporadas[i+1] = []
    for json in response:
        season = int(json['season'])
        temporadas[season].append(json)
    if serie == "Breaking+Bad":
        serie = "Breaking Bad"
    else:
        serie = "Better Call Saul"
    return render(request, 'Temporadas.html', {'temporadas':temporadas, 'serie': serie})

def episodios(request, episode_id):
    response = requests.get(f'https://tarea-1-breaking-bad.herokuapp.com/api/episodes/{episode_id}').json()
    print(response)
    return render(request, 'Episodio.html', {'response':response[0]})