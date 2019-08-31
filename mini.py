from flask import Flask
from flask_restplus import Api, Resource, fields
from flask import url_for
from flask_cors import CORS

import os

app = Flask(__name__)
app.url_map.strict_slashes = False
app.debug = True


api = Api(
    app,
    title='아산',
    version='1.0',
    description="아산"
)

ns = api.namespace('gym', description='체육관')


res = ns.model('GymRes', {
    'user_name': fields.String(required=True),
    'gym_name': fields.String(required=True),
})


gym = ns.model('Gym', {
    'gym': fields.String(required=True)
})
gym_list = ns.model('GymList', {
    'gym_list': fields.List(fields.Nested(gym))
})


@ns.route('/')
class Gym(Resource):
    @ns.expect(res)
    def post(self):
        data = api.payload

        fid = open("gym.txt", "a")

        if not os.path.isfile(filepath):
            fid.write(data['gym_name'] + data['user_name'])
        fid.close()

    @ns.marshal_with(gym)
    def get(self):
        fid = open("gym.txt", "r")
        data = []
        for line in fid.readlines():
            data.append(line)
        return {'gym_list': data}, 200


