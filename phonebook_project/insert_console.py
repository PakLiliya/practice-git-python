# insert_console.py
import psycopg2
from config import load_config

def insert_from_console():
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Ввод данных пользователем
                first_name = input("Enter first name: ")
                last_name = input("Enter last name (optional): ")
                phone = input("Enter phone number: ")

                # SQL запрос на вставку
                cur.execute(
                    "INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)",
                    (first_name, last_name, phone)
                )
                print("Data inserted successfully!")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == "__main__":
    insert_from_console()