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

    except Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        # Close cursor and connection safely
        try:
            if cursor.is_connected():
                cursor.close()
        except:
            pass

        try:
            if connection.is_connected():
                connection.close()
        except:
            pass


if __name__ == "__main__":
    create_database()
