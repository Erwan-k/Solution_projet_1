
from flask_restful import Resource, reqparse
from utils import approximation_lagrange
from operations import ecrire_polynome

points_post_args = reqparse.RequestParser()
points_post_args.add_argument("x",type=int,required=True)
points_post_args.add_argument("y",type=int,required=True)
points_delete_args = reqparse.RequestParser()
points_delete_args.add_argument("x",type=int,required=True)
points_delete_args.add_argument("y",type=int,required=True)

liste_points = []

class points(Resource):
	def get(self):
		global liste_points
		return {"retour":"ok","liste_points":liste_points}

	def post(self):
		body = points_post_args.parse_args()
		[x,y] = [body[i] for i in body]

		global liste_points
		liste_points += [[x,y]]

		return {"retour":"ok"}

	def delete(self):
		body = points_delete_args.parse_args()
		[x,y] = [body[i] for i in body]

		global liste_points
		if liste_points.count([x,y]):
			liste_points.remove([x,y])

		return {"retou":"ok"}

class polynome(Resource):
	def get(self):

		global liste_points
		return ecrire_polynome(approximation_lagrange(liste_points))

