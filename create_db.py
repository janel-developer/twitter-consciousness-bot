import db_connect
import datetime
from psycopg2 import Error

def create_twinspirations_table():
  try:
    connection = db_connect.connect_to_db()
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE twinspirations (
      id SERIAL PRIMARY KEY,
      twinspiration VARCHAR(280),
      last_sent TIMESTAMP); ''')
    cursor.close()
    connection.commit()
  except (Exception, Error) as error:
    print(f'Failed to create twinspiration table: {error}')
  finally:
    if (connection):
      if (cursor):
        cursor.close()
      connection.close()

def insert_twinspiration(cursor, twinspiration):
  # Use an old date so these new sayings are used next
  record_to_insert = (twinspiration, datetime.datetime(2019, 1, 1))
  try:
    cursor.execute('''INSERT INTO twinspirations (TWINSPIRATION, LAST_SENT) VALUES (%s,%s)''', record_to_insert)
  except (Exception, Error) as error:
    print(f'Could not insert {twinspiration}: {error}')
    raise(error)

def populate_twinspirations(twinspirations):
  connection = db_connect.connect_to_db()
  cursor = connection.cursor()
  try:
    for twinspiration in twinspirations:
      insert_twinspiration(cursor, twinspiration)
    connection.commit()
  except (Exception, Error) as error:
    print(f'Failed to populate twinspirations: {error}')
  finally:
    if (connection):
      if (cursor):
        cursor.close()
      connection.close()

def read_from_file(filename):
  # Open a file for reading in new sayings to put in the table
  twinspirations = []
  f=open(filename)
  lines=f.readlines()
  for line in lines:
    twinspirations.append(line)
  f.close()
  return twinspirations

create_twinspirations_table()
populate_twinspirations(read_from_file("twinspirations.txt"))