import sqlite3
from sqlite3 import Error


# connection = sqlite3.connect('patients.db')
# cursor = connection.cursor()

# create_table = "CREATE TABLE IF NOT EXISTS patients (id integer primary key autoincrement,latitude real,longitude real)"


# cursor.execute(create_table)
# connection.commit()
# connection.close()


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)

    except Error as e:
        print(e)


def create_patient(conn, patient):
    """
    Create a new task
    :param conn:
    :param patient:
    :return:
    """
    sql = ''' INSERT INTO patients(id,name,surname,bed,age,doctor)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, patient)
    conn.commit()
    return cur.lastrowid


def main():
    database = r"/Volumes/AH/Flask-REST-Api-for-Kotlin-main/db.db"
    sql_create_patients_table = """CREATE TABLE IF NOT EXISTS patients (
                                     id integer PRIMARY KEY NOT NULL,
                                     name text NOT NULL,
                                     surname text NOT NULL,
                                     bed integer,
                                     age integer,
                                     doctor integer NOT NULL
                                 );"""

    conn = create_connection(database)
    if conn is not None:
        create_table(conn, sql_create_patients_table)

        with conn:
            patient1 = (1, 'adam', 'h', 1, 1997, 1)
            patient2 = (2, 'zuza', 'd', 2, 1998, 2)
            patient3 = (3, 'arnold', 's', 3, 1945, 3)
            patient4 = (4, 'dave', 'g', 4, 1962, 4)
            patient5 = (5, 'martin', 'g', 4, 1962, 4)
            patient6 = (6, 'andy', 'f', 4, 1962, 4)
            patient7 = (7, 'alan', 'w', 4, 1962, 4)

            create_patient(conn, patient1)
            create_patient(conn, patient2)
            create_patient(conn, patient3)
            create_patient(conn, patient4)
            create_patient(conn, patient5)
            create_patient(conn, patient6)
            create_patient(conn, patient7)

    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
