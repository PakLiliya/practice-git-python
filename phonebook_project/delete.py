import psycopg2
from config import load_config

def delete_contact(contact_id):
    """ Удалить контакт по ID """
    sql = "DELETE FROM phonebook WHERE id = %s"
    config = load_config()
    deleted_rows = 0
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (contact_id,))
                deleted_rows = cur.rowcount
                conn.commit()
                print(f"Deleted {deleted_rows} row(s).")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return deleted_rows

if __name__ == '__main__':
    delete_contact(2)