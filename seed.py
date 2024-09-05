import sqlite3
from faker import Faker
from random import randint


def generate_fake_data():
    # Константи
    NUM_TASKS = 100  # Кількість фейкових завдань, які потрібно згенерувати
    NUM_USERS = 10  # Кількість користувачів, для яких потрібно згенерувати завдання

    # Ініціалізація Faker
    fake_data = Faker()

    # Генерація фейкових користувачів
    fake_users = [(fake_data.name(), fake_data.email()) for _ in range(NUM_USERS)]

    # Генерація фейкових завдань
    fake_tasks = []
    for _ in range(NUM_TASKS):
        fake_tasks.append((
            fake_data.sentence(nb_words=3),  # title
            fake_data.text(max_nb_chars=200),  # description
            randint(1, 3),  # status_id (1: new, 2: in progress, 3: completed)
            randint(1, NUM_USERS)  # user_id
        ))

    # Статуси
    statuses = [('new',), ('in progress',), ('completed',)]

    return fake_users, fake_tasks, statuses

# Вставка фейкових даних
def insert_data_to_db(fake_users, fake_tasks, statuses):
    with sqlite3.connect('tables.db') as conn:
        cur = conn.cursor()
        
        # Вставка статусів
        sql_query_for_status = 'INSERT INTO status (name) VALUES (?)'
        cur.executemany(sql_query_for_status, statuses)

        # Вставка фейкових користувачів у таблицю users
        sql_query_for_users = 'INSERT INTO users (fullname, email) VALUES (?, ?)'
        cur.executemany(sql_query_for_users, fake_users)

        # Вставка фейкових завдань у таблицю tasks
        sql_query_for_tasks = 'INSERT INTO tasks (title, description, status_id, user_id) VALUES (?, ?, ?, ?)'
        cur.executemany(sql_query_for_tasks, fake_tasks)

        # Збереження змін
        conn.commit()

# Основна функція
if __name__ == '__main__':
    fake_users, fake_tasks, statuses = generate_fake_data()
    insert_data_to_db(fake_users, fake_tasks, statuses)
    print("Фейкові дані успішно внесені в базу даних.")