from flask import Flask, Response, request, abort
# import json dependencies
from flask import json, jsonify
from flask_restx import Api, Resource, fields


app = Flask(__name__)
#Initialize Flask application entry point
api = Api(app)
#Add a namespace factory. This registers resources for the current API instance.
ns_movies = api.namespace('ns_movies', description = 'Movies API')


#Load JSON data to the application
f = open("./movies.json", "r")
loaded_json = json.load(f)
movie_info = {
  	'{{0}}-{{1}}'.format(dct["title"], dct["year"]): dct for dct in loaded_json.get("movies_list")
}

#create the data model
movie_data = api.model(

  'Movie Data', {
    "title": fields.String(description = "Title of movie", required = True),
    "year": fields.Integer(description = "Year released", required = True),
    "cast": fields.List(fields.String, description = "Cast of movie", required = True),
    "image": fields.Url(description = "Image Url", required = True),
    "description": fields.String(description = "Description of movie", required = True)
  }
)

#First, create the access route
@ns_movies.route("/")
#add the data source
class movies(Resource):
	def get(self):
	  return jsonify(movie_info)

	@api.expect(movie_data)
	def post(self):
		params = request.get_json()
		t = params.get("title", "")
		y = params.get("year", "")
		if (t) and (y):
			try:
				new_id = '{t}-{y}'
				if new_id in movie_info.keys():
					abort(status = 409, description = 'Already Exists.')

				movie_info[new_id] = params
				for p in params:
				  if p not in movie_data.keys():
				  	raise KeyError
			except:
				abort(status = 400, description = 'Bad parameters')
		else:
			abort(status = 400, description = 'Missing Title or Year.')
		return Response(status = 200)

@ns_movies.route("/<string:id>")
class movies(Resource):
	def get(self, id):
		if id not in movie_info:
			abort(status = 404, description = "Movie {id} doesn't exists.")
		return movie_info.get(id)

	#PUT to update specific movie details.
	@api.expect(movie_info)
	def put(self, id):
		if id not in movie_info:
			abort(status = 404, description = "Movie {id} doesn't exists.")
		params = request.get_json()
		if not(params):
			abort(status = 400, description = 'No parameters')

		for p in params:
		  if p not in movie_data.keys():
		  	abort(status = 400, description = 'Bad parameters')
		for p in params:
		  movie_info[id][p] = params[p]
		return Response(status = 200)

	def delete(self, id):
		try:
	  		del movie_info[id]
		except KeyError:
	  		abort(status = 404, description = "Movie {id} doesn't exists.")
		return Response(status = 200)


if __name__ == "__main__":
  #run the app on localhost
  app.run(host = '0.0.0.0', debug = True, port="3334")