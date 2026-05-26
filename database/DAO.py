from database.DB_connect import DBConnect
from model.fermata import Fermata
from model.connessione import Connessione


class DAO():

    @staticmethod
    def getAllFermate():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM fermata"
        cursor.execute(query)

        for row in cursor:
            result.append(Fermata(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def hasconn(u: Fermata,v: Fermata):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = ("SELECT * FROM connessione c WHERE c.id_stazP=%s AND c.id_stazA=%s")
        cursor.execute(query,(u.id_fermata,v.id_fermata))

        for row in cursor:
            result.append(row)
        cursor.close()
        conn.close()
        return len(result) >0 #maggiore di 0 ritorna true

    @staticmethod
    def getVicini(u: Fermata):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "select * from connessione c where c.id_stazP = %s"
        cursor.execute(query, (u.id_fermata,))

        for row in cursor:
            result.append(Connessione(
        row["id_connessione"],
        row["id_linea"],
        row["id_stazP"],
        row["id_stazA"]
    ))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def hasconn(u: Fermata, v: Fermata):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = ("SELECT * FROM connessione c WHERE c.id_stazP=%s AND c.id_stazA=%s")
        cursor.execute(query, (u.id_fermata, v.id_fermata))

        for row in cursor:
            result.append(row)
        cursor.close()
        conn.close()
        return len(result) > 0  # maggiore di 0 ritorna true

    @staticmethod
    def getAllFermatePesati():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT id_stazP, id_stazA,count(*) as peso
        FROM connessione c
        GROUP BY id_stazA, id_stazP
        ORDER BY peso desc"""
        cursor.execute(query)

        for row in cursor:
            result.append((row["id_stazP"], row["id_stazA"], row["peso"]))
        cursor.close()
        conn.close()
        return result
