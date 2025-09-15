import mysql.connector
from geopy import distance

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="käyttis",
    password="salis",
    autocommit=True
)

def get_coordinates(code):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport where ident =  '{code}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if not result:
        return "Ei löydy"
    return result


ICAO_koodi1 = input("Syötä ensimmäisen kentän ICAO-koodi: ").upper()
ICAO_koodi2 = input("Syötä toisen kentän ICAO-koodi: ").upper()
coordinates1 = get_coordinates(ICAO_koodi1)
coordinates2 = get_coordinates(ICAO_koodi2)
print(f"Kohteiden {ICAO_koodi1} ja {ICAO_koodi2} välinen etäisyys on {distance.distance(coordinates1, coordinates2).km:.2f} km")
