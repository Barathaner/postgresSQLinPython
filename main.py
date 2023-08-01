import psycopg2

conn = psycopg2.connect(host='127.0.0.1', dbname = "postgres", user = "Arina", password = "1234", port = 5432)

cur = conn.cursor()

cur.execute("""Create Table if not exists person(
            id INT Primary key,
            name VARCHAR(255),
            age INT,
            gender CHAR
);
""")

#do sth

conn.commit()

cur.close()
conn.close()