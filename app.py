from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Brad Richardson in 3308!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://brad_lab_10_postgresql_user:MBvCTh8jJemI9zbgrZ3uu46pXCfrnFzU@dpg-cqjsrh8gph6c739ds0i0-a/brad_lab_10_postgresql")
    conn.close()
    return 'Database connection successful!'