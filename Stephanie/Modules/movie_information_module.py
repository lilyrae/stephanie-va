import omdb
from Stephanie.Modules.base_module import BaseModule


class MovieInformationModule(BaseModule):
    def __init__(self, *args):
        super(MovieInformationModule, self).__init__(*args)

    def give_some_information(self):
        self.assistant.say("which movie would you like to know about?")
        movie_name = self.assistant.listen().decipher()
        movies = omdb.search_movie(movie_name)
        if len(movies) > 0:
            movies.sort(key=lambda x: x.year, reverse=True)
            for i in range(0, len(movies)):
                if i == 0:
                    speech = _("movie.ask_confirmation").format(
                        movies[i].title, movies[i].year)
                else:
                    speech = _("movie.suggest").format(
                        movies[i].title, movies[i].year)
                self.assistant.say(speech)
                response = self.assistant.listen().decipher()
                if len(response.split()) > 3:
                    return _("movie.moody")
                elif response == "yes":
                    imdb_id = movies[i].imdb_id
                    print(_("found"))
                    return self.give_movie_information_from_imdb_id(imdb_id)
        else:
            return _("movie.ask_repeat")

    @staticmethod
    def give_movie_information_from_imdb_id(imdb_id):
        movie = omdb.imdbid(imdb_id)
        speech = _("movie.report").format(
            movie.title,
            movie.released,
            movie.director,
            movie.genre,
            movie.runtime,
            movie.imdb_rating,
            movie.actors,
            movie.plot
        )
        return speech
