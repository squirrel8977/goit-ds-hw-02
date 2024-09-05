
import sqlite3

def query_execution(sql_list):
    with sqlite3.connect('tables.db') as con:
        cur = con.cursor()
        results = []
        for sql in sql_list:
            cur.execute(sql)
            results.append(cur.fetchall())
    return results

sql_queries = [
    '''SELECT * FROM tasks WHERE user_id=9''',
    '''SELECT tasks.id, tasks.title FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = 'new')''',
    '''UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = 'in progress') WHERE id = 10''',
    '''SELECT fullname FROM users WHERE id NOT IN (SELECT user_id FROM tasks)''',
    '''INSERT INTO tasks(title, description, status_id, user_id) VALUES('Task', 'Task description', (SELECT id FROM status WHERE name='completed'), 3)''',
    '''SELECT tasks.id, tasks.title FROM tasks WHERE status_id NOT IN (SELECT id FROM status WHERE name='completed')''',
    '''DELETE FROM tasks WHERE id=35''',
    '''SELECT us.id, us.fullname, us.email FROM users as us WHERE us.email LIKE "%@example.org"''',
    '''UPDATE users SET fullname = "Cristiano MEssi" WHERE id = 7''',
    '''SELECT status.name, COUNT(tasks.id) as task_count FROM tasks JOIN status ON tasks.status_id = status.id GROUP BY status.name''',
    '''SELECT tasks.id, tasks.title, tasks.description, tasks.status_id, tasks.user_id FROM tasks JOIN users ON tasks.user_id = users.id WHERE users.email LIKE "%@example.com"''',
    '''SELECT title FROM tasks WHERE description IS NULL''',
    '''SELECT t.title AS title, u.fullname AS user_name, s.name AS status FROM tasks AS t INNER JOIN users AS u ON t.user_id = u.id INNER JOIN status AS s ON t.status_id = s.id WHERE s.name = "in progress"''',
    '''SELECT u.fullname AS user_name, COUNT(t.id) AS task_count FROM users AS u LEFT JOIN tasks AS t ON u.id = t.user_id GROUP BY u.id, u.fullname'''
]

if __name__ == '__main__':
    results = query_execution(sql_queries)
    for result in results:
        print(result)