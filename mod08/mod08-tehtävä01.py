import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="käyttis",
    password="salis",
    autocommit=True
)

def get_name_and_municipality(code):
    sql = f"SELECT name, municipality FROM airport where ident =  '{code}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if not result:
        return "Ei löydy"
    return result

ICAO_koodi = input("Syötä ICAO-koodi: ").upper()
name_municipality = get_name_and_municipality(ICAO_koodi)
print(f"Lentokentän {ICAO_koodi}: nimi ja sijainti: {name_municipality}")
