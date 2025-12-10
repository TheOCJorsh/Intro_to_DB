import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (NOT to any specific database)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="nam1234"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database (won't fail if it already exists)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            connection.commit()

            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

 
    except Error as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        # Close cursor safely
        if cursor is not None:
            try:
                cursor.close()
            except:
                pass

        # Close connection safely
        if connection is not None:
            try:
                connection.close()
            except:
                pass


if __name__ == "__main__":
    create_database()