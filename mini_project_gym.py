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

CORS(app)


@property
def specs_url(self):
        return url_for(self.endpoint('specs'), _external=True, _scheme='https')


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
        print(data['gym_name'])
        fid.write(data['gym_name'] + ": " + data['user_name'] + '\n')
        fid.close()

    @ns.marshal_with(gym_list)
    def get(self):
        fid = open("gym.txt", "r")
        data = []
        for line in fid.readlines():
            data.append({'gym': line[:-1]})
        print(data)
        return {'gym_list': data}, 200

app.run(host='0.0.0.0', port=5000, debug=True) 
