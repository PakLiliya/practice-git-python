# update_phonebook.py
import psycopg2
from config import load_config

def update_contact(contact_id, first_name=None, last_name=None, phone=None):
    """Update a contact in the phonebook table by id"""
    fields = []
    values = []
    
    if first_name:
        fields.append("first_name = %s")
        values.append(first_name)
    if last_name:
        fields.append("last_name = %s")
        values.append(last_name)
    if phone:
        fields.append("phone = %s")
        values.append(phone)
    
    if not fields:
        print("No fields to update")
        return 0
    
    # формируем SQL
    sql = f"UPDATE phonebook SET {', '.join(fields)} WHERE id = %s"
    values.append(contact_id)
    
    updated_rows = 0
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, tuple(values))
                updated_rows = cur.rowcount
                conn.commit()
                print(f"Updated {updated_rows} row(s)")
    except Exception as error:
        print(error)
    return updated_rows

if __name__ == "__main__":
    # пример: меняем имя и телефон контакта с id=1
    update_contact(1, first_name="Johnathan", phone="+19876543210")