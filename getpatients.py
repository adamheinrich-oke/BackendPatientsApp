import sqlite3

from flask_restful import Resource


class GetPatients(Resource):

    @classmethod
    def find(cls, _id):
        connection = sqlite3.connect('db.db')
        cursor = connection.cursor()
        query = "select * from patients WHERE id = ?"
        result = cursor.execute(query, (id,)).fetchall()
        if result:
            connection.close()
            return {"message": result}, 201
        return {"message:": "error"}, 400

    def get(self, doctor):
        connection = sqlite3.connect('db.db')
        cursor = connection.cursor()
        query = "select * from patients WHERE doctor = ?"
        result = cursor.execute(query, (doctor,)).fetchall()
        if result:
            connection.close()
            return {"message": result}, 201
        return {"message": "failure"}, 400
