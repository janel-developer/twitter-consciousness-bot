import db_connect
import twitter_auth
from psycopg2 import Error

# Returns a record from the twinspirations table with the oldest last_sent date
def get_twinspiration():
  connection = db_connect.connect_to_db()
  cursor = connection.cursor()
  twinspiration = ""
  try:
    cursor.execute('''SELECT id,twinspiration FROM twinspirations ORDER BY last_sent LIMIT 1;''')
    twinspirations = cursor.fetchall()
  except (Exception, Error) as error:
    print("Error while fetching data from DB", error)
  finally:
    # closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
  return twinspirations[0]

# Updates the last_sent field of the record to now for the message that was sent in the status
def update_last_sent(id):
  connection = db_connect.connect_to_db()
  cursor = connection.cursor()
  try:
    cursor.execute('''UPDATE twinspirations SET last_sent = %s WHERE id = %s''', ("now", id))
    connection.commit()
  except (Exception, Error) as error:
    print("Error while updating last_sent", error)
  finally:
    # closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


twinspiration = get_twinspiration()
# The id is used to update the last_sent
id = twinspiration[0]
# The message is used to update the status
message = twinspiration[1]

# Authorize using the twitter_auth module (included here)
api = twitter_auth.auth()
# Call the update_status tweepy api
api.update_status(message)
print(f'Send message: {message}')
update_last_sent(id)
