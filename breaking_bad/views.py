from django.shortcuts import render
from django.http import HttpResponse
import requests
import datetime


# Create your views here.
def home(request):
    return render(request, 'Home.html')

def temporadas(request, serie, num_temp):
    response = requests.get(f'https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series={serie}').json()
    temporadas = {}
    numero_temporadas = int(response[len(response)-1]['season'])
    for i in range(numero_temporadas):
        temporadas[i+1] = []
    for json in response:
        season = int(json['season'])
        temporadas[season].append(json)
    return render(request, 'Temporadas.html', {'temporadas':temporadas, 'serie': serie})

def episodios(request, serie, episode_id):
    response = requests.get(f'https://tarea-1-breaking-bad.herokuapp.com/api/episodes/{episode_id}').json()
    response[0]["air_date"] = datetime.datetime.strptime(response[0]["air_date"], '%Y-%m-%dT%H:%M:%S.%fZ').strftime("%d/%m/%Y")
    return render(request, 'Episodio.html', {'serie':serie, 'episodio':response[0]})

def personajes(request, serie, character_name):
    response = requests.get(f'https://tarea-1-breaking-bad.herokuapp.com/api/characters?name={character_name}').json()
    last_ocup = response[0]["occupation"][len(response[0]["occupation"])-1]
    new_ocups = []
    for ocup in response[0]["occupation"]:
        if ocup != last_ocup:
            new_ocups.append(str(ocup)+", ")
        else:
            new_ocups.append(str(ocup))
    response[0]["occupation"] = new_ocups

    response_citas = requests.get(f'https://tarea-1-breaking-bad.herokuapp.com/api/quote?author={character_name}').json()
    
    return render(request, 'Personaje.html', {'serie':serie, 'personaje':response[0], 'citas': response_citas})