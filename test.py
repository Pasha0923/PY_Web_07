import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="hw_orm",
    user="postgres",
    password="Postgres123"
)

print("OK")