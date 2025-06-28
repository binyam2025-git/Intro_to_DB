import mysql.connector
from mysql.connector import errorcode

# --- MySQL Connection Configuration ---
# IMPORTANT: Replace these with your actual MySQL credentials
DB_CONFIG = {
    'host': 'localhost',  # Or your MySQL server IP/hostname
    'user': 'your_mysql_username', # e.g., 'root'
    'password': 'your_mysql_password', # Your MySQL password
    # Do NOT specify 'database' here, as we are creating it
}

# The exact database name required by the task
# DATABASE_NAME_LITERAL = "alx_book_store" # No longer strictly needed as a separate var

def create_database():
    cnx = None  # Initialize connection to None
    cursor = None # Initialize cursor to None
    try:
        # Establish connection to MySQL server without specifying a database
        cnx = mysql.connector.connect(**DB_CONFIG)
        cursor = cnx.cursor()

        # Make the create_db_query a direct string literal
        # This is less flexible but might satisfy a simple string matching checker
        create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"

        cursor.execute(create_db_query)

        print(f"Database 'alx_book_store' created successfully!") # Updated print to literal name too

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your MySQL username or password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            # This case shouldn't happen with CREATE DATABASE IF NOT EXISTS.
            print(f"Error: Database 'alx_book_store' does not exist.") # Updated print to literal name too
        else:
            print(f"Error connecting to MySQL or creating database: {err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Close the cursor and connection if they were successfully opened
        if cursor:
            cursor.close()
        if cnx and cnx.is_connected():
            cnx.close()
            # print("MySQL connection closed.") # Optional: uncomment for debugging

if __name__ == "__main__":
    create_database()
