import mysql.connector
from mysql.connector import errorcode

# --- MySQL Connection Configuration ---
# IMPORTANT: Replace these with your actual MySQL credentials
DB_CONFIG = {
    'host': 'localhost',  # Or your MySQL server IP/hostname
    'user': 'root', # e.g., 'root'
    'password': 'Bin@0911455745', # Your MySQL password
    # Do NOT specify 'database' here, as we are creating it
}

DATABASE_NAME = "alx_book_store"

def create_database():
    cnx = None  # Initialize connection to None
    try:
        # Establish connection to MySQL server without specifying a database
        # This is necessary to execute CREATE DATABASE
        cnx = mysql.connector.connect(**DB_CONFIG)
        cursor = cnx.cursor()

        # SQL statement to create the database if it doesn't exist
        # Using IF NOT EXISTS handles the case where the database already exists
        # without needing SELECT or SHOW.
        create_db_query = f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME}"

        cursor.execute(create_db_query)

        print(f"Database '{DATABASE_NAME}' created successfully!")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your MySQL username or password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            # This case shouldn't happen with CREATE DATABASE IF NOT EXISTS,
            # but good to have for other queries.
            print(f"Error: Database '{DATABASE_NAME}' does not exist.")
        else:
            print(f"Error connecting to MySQL or creating database: {err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Close the connection if it was successfully opened
        if cnx and cnx.is_connected():
            cursor.close()
            cnx.close()
            # print("MySQL connection closed.") # Optional: uncomment for debugging

if __name__ == "__main__":
    create_database()
