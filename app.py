from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Data awal film
films = {
    "1": {
        "title": "Inception",
        "director": "Christopher Nolan",
        "release_year": 2010,
        "genre": "Science Fiction",
        "rating": 8.8
    },
    "2": {
        "title": "The Shawshank Redemption",
        "director": "Frank Darabont",
        "release_year": 1994,
        "genre": "Drama",
        "rating": 9.3
    },
    "3": {
        "title": "The Godfather",
        "director": "Francis Ford Coppola",
        "release_year": 1972,
        "genre": "Crime",
        "rating": 9.2
    },
    "4": {
        "title": "Pulp Fiction",
        "director": "Quentin Tarantino",
        "release_year": 1994,
        "genre": "Crime",
        "rating": 8.9
    },
    "5": {
        "title": "The Dark Knight",
        "director": "Christopher Nolan",
        "release_year": 2008,
        "genre": "Action",
        "rating": 9.0
    }
}

# Kelas untuk menangani operasi CRUD
class FilmList(Resource):
    def get(self):
        return {
            "error": False,
            "message": "Success",
            "count": len(films),
            "films": films
        }

class FilmDetail(Resource):
    def get(self, film_id):
        if film_id in films:
            return {
                "error": False,
                "message": "Success",
                "film": films[film_id]
            }
        return {"error": True, "message": "Film not found"}, 404

class AddFilm(Resource):
    def post(self):
        data = request.get_json()
        film_id = str(len(films) + 1)
        new_film = {
            "title": data.get("title"),
            "director": data.get("director"),
            "release_year": data.get("release_year"),
            "genre": data.get("genre"),
            "rating": data.get("rating")
        }
        films[film_id] = new_film
        return {
            "error": False,
            "message": "Film added successfully",
            "film": new_film
        }, 201

class UpdateFilm(Resource):
    def put(self, film_id):
        if film_id in films:
            data = request.get_json()
            film = films[film_id]
            film["title"] = data.get("title", film["title"])
            film["director"] = data.get("director", film["director"])
            film["release_year"] = data.get("release_year", film["release_year"])
            film["genre"] = data.get("genre", film["genre"])
            film["rating"] = data.get("rating", film["rating"])
            return {
                "error": False,
                "message": "Film updated successfully",
                "film": film
            }
        return {"error": True, "message": "Film not found"}, 404

class DeleteFilm(Resource):
    def delete(self, film_id):
        if film_id in films:
            deleted_film = films.pop(film_id)
            return {
                "error": False,
                "message": "Film deleted successfully",
                "film": deleted_film
            }
        return {"error": True, "message": "Film not found"}, 404

api.add_resource(FilmList, '/films')
api.add_resource(FilmDetail, '/films/<string:film_id>')
api.add_resource(AddFilm, '/films/add')
api.add_resource(UpdateFilm, '/films/update/<string:film_id>')
api.add_resource(DeleteFilm, '/films/delete/<string:film_id>')

if __name__ == '__main__':
    app.run(debug=True)
