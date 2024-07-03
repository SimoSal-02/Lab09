from database.DB_connect import DBConnect
from model.aeroporto import Aeroporto

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllAeroporti():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct *
                from airports a """

        cursor.execute(query)
        for row in cursor:
            result.append(Aeroporto(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllConnessioniTraAeroporti(mappaAeroporti,miglia):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select 
                least( f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID) as a1,
                greatest( f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID) as a2,
                SUM(f.DISTANCE) as totDistance, 
                COUNT(*) as nVoli 
                from flights f
                group by 
                least(f.ORIGIN_AIRPORT_ID,f.DESTINATION_AIRPORT_ID),
                greatest(f.ORIGIN_AIRPORT_ID,f.DESTINATION_AIRPORT_ID)"""
        """
        LEAST(ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID): Questa funzione restituisce il minore tra i due ID degli aeroporti,
         garantendo che l'aeroporto con l'ID minore venga sempre considerato come a1.
        GREATEST(ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID): Questa funzione restituisce il maggiore tra i due ID degli aeroporti,
         garantendo che l'aeroporto con l'ID maggiore venga sempre considerato come a2."""

        cursor.execute(query)

        for row in cursor:
            media = float(row["totDistance"]/row["nVoli"])
            print(type(media))
            print(type(miglia))
            if media > float(miglia):
                result.append((mappaAeroporti[row["a1"]], mappaAeroporti[row["a2"]],{'weight':media}))


        cursor.close()
        conn.close()
        return result
