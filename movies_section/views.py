from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

import requests

# Create your views here.


class MovieDetailView(View):
    base_url = "https://api.themoviedb.org/3/"
    api_key = "5284abc60d5eabb9e9ef7d55ec98e136"

    def get(self, request, movie_id):
        url = self.base_url + 'movie/' + movie_id
        res = requests.get(url, params={ "api_key": self.api_key })
        data = res.json()
        url = self.base_url + 'movie/' + movie_id + '/similar'
        similar_movies = requests.get(url, params={ "api_key": self.api_key })
        similar_movies_data = similar_movies.json()["results"]
        return render(request, 'movies_section/movie-detail.html', { 'movie_data' : data, 'movies_data': similar_movies_data })


class MovieView(View):

    base_url = "https://api.themoviedb.org/3/"
    api_key = "5284abc60d5eabb9e9ef7d55ec98e136"

    def get(self, request):
        return render(request, "movies_section/index.html", {"movies_active": "active", "show_movies_data" : False})

    def post(self, request):
        try:
            movie_name = request.POST["movie"]
            url = self.base_url + "search/movie"
            res = requests.get(url=url, params={"api_key": self.api_key, "query": movie_name})
            data = res.json()["results"]
            return render(request, "movies_section/index.html", {"movies_active": "active", 'show_movies_data': True, "movies_data": data})
        except:
            return render(request, "movies_section/index.html", {"movies_active": "active", "show_movies_data" : False})
