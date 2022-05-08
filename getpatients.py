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
        patientsarray = []
        apiresponse = []
        if result:
            for elem in result:
                patient = {
                    "id": elem[0],
                    "name": elem[1],
                    "surname": elem[2],
                    "bed": elem[3],
                    "age": elem[4],
                    "doctor": elem[5],
                    "image": elem[6]
                }
                patientsarray.append(patient)

            for patient in patientsarray:
                patient = {"patient": patient}
                apiresponse.append(patient)

            connection.close()
            return apiresponse, 201
        return {"message": "failure"}, 400
