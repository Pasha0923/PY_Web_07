import psycopg2

try:
    conn = psycopg2.connect("")
except Exception as e:
    print(type(e))
    print(e)