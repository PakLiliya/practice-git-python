import psycopg2
from config import load_config

def get_contact_by_id(contact_id):
    """ Получить контакт по ID """
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT id, first_name, last_name, phone
                    FROM phonebook
                    WHERE id = %s
                """, (contact_id,))
                row = cur.fetchone()
                if row:
                    print("Contact:", row)
                else:
                    print("Contact not found.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def get_all_contacts():
    """ Получить все контакты """
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id, first_name, last_name, phone FROM phonebook ORDER BY id")
                rows = cur.fetchall()
                for row in rows:
                    print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    print("All contacts:")
    get_all_contacts()
    print("\nContact with ID=1:")
    get_contact_by_id(1)