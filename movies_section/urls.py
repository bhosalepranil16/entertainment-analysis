from django.urls import path


from . import views

urlpatterns = [
    path('', views.MovieView.as_view(), name='movies-section'),
    path('<str:movie_id>', views.MovieDetailView.as_view(), name='movie-detail')
]
