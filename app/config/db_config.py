import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="bey6mxf7gh4lyym095un-mysql.services.clever-cloud.com",
        user="u0huhbmrv4yz5qxw",
        password="CDHANgsKyqnUB4F4zlUS",
        database="bey6mxf7gh4lyym095un"
    )