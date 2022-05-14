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
    sql = ''' INSERT INTO patients(id,name,surname,bed,age,doctor,image)
              VALUES(?,?,?,?,?,?,?) '''
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
                                     doctor integer NOT NULL,
                                     image text NOT NULL
                                 );"""

    conn = create_connection(database)
    if conn is not None:
        create_table(conn, sql_create_patients_table)

        with conn:
            patient1 = (1, 'adam', 'h', 1, 1997, 1,
                        "https://images.unsplash.com/photo-1611915387288-fd8d2f5f928b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8MXx8fGVufDB8fHx8&w=1000&q=80")
            patient2 = (2, 'zuza', 'd', 2, 1998, 2,
                        "https://images.unsplash.com/photo-1611915387288-fd8d2f5f928b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8MXx8fGVufDB8fHx8&w=1000&q=80")
            patient3 = (3, 'arnold', 's', 3, 1945, 3,
                        "https://images.unsplash.com/photo-1611915387288-fd8d2f5f928b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8MXx8fGVufDB8fHx8&w=1000&q=80")
            patient4 = (4, 'Dave', 'Gahan', 9, 1962, 4,
                        "https://cdn.koncertomania.pl/file/eventmediabackup/15/1/1420337343AKHqyYqhs7qQOrGZc5QYEa6Kq87aBW.jpg")
            patient5 = (5, 'Martin', 'Gore', 10, 1961, 4,
                        "https://www.magneticmag.com/.image/t_share/MTYzNTc3ODgyMDM4MjQ4ODc1/62182da3-149b-4ba7-9e02-5b6b084a6da2.jpg")
            patient6 = (6, 'Andy', 'Fletcher', 11, 1961, 4,
                        "https://ocdn.eu/pulscms-transforms/1/FAqk9kuTURBXy9iZGNmNDU4YS0zNzZjLTRlZjMtODhjMi02ZWRkMDMwYmNkYWYuanBlZ5GVAs0DBwDDw4GhMAE")
            patient7 = (7, 'Alan', 'Wilder', 12, 1959, 4,
                        "https://dt7v1i9vyp3mf.cloudfront.net/styles/news_large/s3/imagelibrary/1/1998-01-alanwilder-1-0KYaRQRLv7qOw6hgaxM0cQzgmlQcGXFS.jpg")

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
