import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Fetch variables
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

data = {
    "user" : USER,
    "password" : PASSWORD,
    "host" : HOST,
    "port" : PORT,
    "dbname" : DBNAME
}

# # Connect to the database
# try:
#     connection = psycopg2.connect(
#         **data
#     )
#     print("Connection successful!")
    
#     # Create a cursor to execute SQL queries
#     cursor = connection.cursor()
    
#     # Example query
#     cursor.execute("SELECT NOW();")
#     result = cursor.fetchone()
#     print("Current Time:", result)

#     # Close the cursor and connection
#     cursor.close()
#     connection.close()
#     print("Connection closed.")

# except Exception as e:
#     print(f"Failed to connect: {e}")
    


def create_user(username,password):
    try:
        conn = psycopg2.connect(**data)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO usuarios (username, password)
            VALUES (%s, %s)
            RETURNING id
        """, (username, password))
        
        user_id = cursor.fetchone()[0]
        cursor.commit()
        return {"id": user_id ,"username": username}
    except Exception as e:
        print(f"Error: {e}")
        cursor.rollback()
    finally:
        cursor.close()
        conn.close()
        

    