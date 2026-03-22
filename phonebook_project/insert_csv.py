# insert_csv.py
import psycopg2
import csv
from config import load_config

def insert_from_csv(filename="data.csv"):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                with open(filename, newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        cur.execute(
                            "INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)",
                            (row['first_name'], row['last_name'], row['phone'])
                        )
                print("CSV data inserted successfully!")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == "__main__":
    insert_from_csv()