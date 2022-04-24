from flask import Flask
from flask_restful import Api

from getpatients import GetPatients
from insertpatients import InsertPatients

app = Flask(__name__)
api = Api(app)
api.add_resource(GetPatients, '/adamapi/get/<string:doctor>', )
api.add_resource(InsertPatients, '/adamapi/post/<string:_id>')

if __name__ == '__main__':
    app.run("0.0.0.0", debug=True, port=3000)
