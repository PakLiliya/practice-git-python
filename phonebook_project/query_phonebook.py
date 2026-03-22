import psycopg2
from config import load_config

def get_contact(contact_id):
    """Retrieve a contact from phonebook by id"""
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id, name, phone FROM phonebook WHERE id = %s", (contact_id,))
                row = cur.fetchone()
                if row:
                    print("Contact:", row)
                else:
                    print("No contact found with id", contact_id)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == "__main__":
    get_contact(1)