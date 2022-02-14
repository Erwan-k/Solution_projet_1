from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from routes.routes import points,polynome

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(points,"/points")
api.add_resource(polynome,"/polynome")

if __name__ == "__main__":
	app.run(debug=True,port=5000,host='0.0.0.0')
