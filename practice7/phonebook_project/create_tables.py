# create_tables.py
import psycopg2
from practice7.config import load_config

def create_tables():
    """Create PhoneBook table in PostgreSQL"""
    # список SQL команд (только реальные SQL-запросы!)
    commands = (
        """
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50),
            phone VARCHAR(20) NOT NULL
        );
        """,
    )

    try:
        # загружаем конфиг
        config = load_config()
        # подключаемся к базе
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    # выполняем только непустые команды
                    if command.strip():
                        cur.execute(command)
                print("PhoneBook table created successfully.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    create_tables()