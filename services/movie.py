from django.db.models import QuerySet

from db.models import Genre, Actor, Movie


def get_movies(genres_ids: int = None,
               actors_ids: int = None
               ) -> QuerySet[Movie] | None:
    if not genres_ids and not actors_ids:
        return Movie.objects.all()
    if genres_ids and actors_ids:
        return Movie.objects.filter(genres__in=genres_ids,
                                    actors__in=actors_ids)
    if genres_ids and not actors_ids:
        return Movie.objects.filter(genres__in=genres_ids)
    if not genres_ids and actors_ids:
        return Movie.objects.filter(actors__in=actors_ids)


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[Genre] = None,
        actors_ids: list[Actor] = None) -> None:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids:
        movie.genres.set(Genre.objects.filter(id__in=genres_ids))
    if actors_ids:
        movie.actors.set(Actor.objects.filter(id__in=actors_ids))
