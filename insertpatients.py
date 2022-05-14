import sqlite3

from flask import request
from flask_restful import Resource


class InsertPatients(Resource):

    def post(self, _id):
        connection = sqlite3.connect('db.db')
        cursor = connection.cursor()
        query = "select * from patients WHERE id = ?"
        result = cursor.execute(query, (_id,)).fetchall()

        if result:
            connection.commit()
            connection.close()
            return {'message': 'Such patient already exists in DB'}, 201
        else:
            data = request.get_json(force=True)
            data = {'id': data['id'], 'name': data['name'], 'surname': data['surname'], 'bed': data['bed'],
                    'age': data['age'], 'doctor': data['doctor'], 'image': data['image']}
            query = "INSERT INTO patients VALUES(?,?,?,?,?,?,?)"
            result = cursor.execute(query,
                                    (data['id'], data['name'], data['surname'], data['bed'], data['age'],
                                     data['doctor'], data['image']))
            connection.commit()
            connection.close()
            if result:
                return {"message": "Posted with success"}, 201
