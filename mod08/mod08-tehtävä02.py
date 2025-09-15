import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="käyttis",
    password="salis",
    autocommit=True
)
def get_type_and_amount(code):
    cursor = connection.cursor()
    cursor.execute(f"SELECT type, COUNT(*) AS total FROM airport WHERE iso_country = '{code}' GROUP BY type;")
    result = cursor.fetchall()
    return result

country_code = input("Syötä maakoodi: ").upper()
print(f"Lentokenttätyypit määrineen: {get_type_and_amount(country_code)}")


