import psycopg2
conn = psycopg2.connect(database="netology_import_phones", user="postgres",
    password="admin", host="localhost", port=5432)

# cur = conn.cursor()
# cur.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, " +
#     "login VARCHAR(64), password VARCHAR(64))")
# conn.commit()