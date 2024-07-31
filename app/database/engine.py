import sqlite3


import sqlite3
import logging
import os
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

DB_PATH = os.path.join(os.path.dirname(__file__), "data.db")

create_table_query = """

CREATE TABLE IF NOT EXISTS link(

    link TEXT

)"""


def intialize_db() -> None:
    """
    Initialize the SQLite database by creating the "link" table if it
    Initialize the SQLite database by creating the "users_info" table if it
    doesn't already exist.

    This function connects to the database, creates the "link" table if it
    doesn't exist, and inserts a default value ("_None_") into the table if
    it is empty.

    Raises:
        sqlite3.Error: If there is a problem with the database.
        Exception: If there is an unexpected error.
    """
    try:
        # Connect to the database
        db = sqlite3.connect(DB_PATH)
        cursor = db.cursor()

        # Create the table if it doesn't already exist
        cursor.execute(create_table_query)

        # Check if the table is empty
        if cursor.execute("SELECT link FROM link").fetchone() is None:
            # Insert a default value into the table
            cursor.execute("INSERT INTO link VALUES ('_None_')")

        # Save the changes to the database
        db.commit()

    # If there is an error, log the error
    except sqlite3.Error as error:
        logger.error(f"Error initializing database: {error}")

    # If there is an unexpected error, log the error
    except Exception as error:
        logger.error(f"Unexpected error initializing database: {error}")

    # Close the database connection
    finally:
        db.close()


def add_link(link: str) -> None:
    """
    Add a link to the database.

    Args:
        link (str): The link to add to the database.

    Raises:
        sqlite3.Error: If there is a problem with the database.
        Exception: If there is an unexpected error.

    This function connects to the database, updates the "link" table with the
    provided link, and saves the changes to the database.
    """
    try:
        # Connect to the database
        db = sqlite3.connect(DB_PATH)
        cursor = db.cursor()

        # Add the link to the database
        # The SQL query updates the "link" field in the "link" table with the
        # provided link
        cursor.execute("UPDATE link SET link = ?", (link,))

        # Save the changes to the database
        db.commit()

    # If there is an error, log the error
    except sqlite3.Error as error:
        logger.error(f"Error adding link to database: {error}")


def add_link(link: str) -> None:
    """
    Add a link to the database.

    Args:
        link (str): The link to add to the database.

    Raises:
        sqlite3.Error: If there is a problem with the database.
        Exception: If there is an unexpected error.

    This function connects to the database, updates the "link" table with the
    provided link, and saves the changes to the database.
    """
    try:
        # Connect to the database
        db = sqlite3.connect(DB_PATH)
        cursor = db.cursor()

        # Add the link to the database
        # The SQL query updates the "link" field in the "link" table with the
        # provided link
        # Execute the SQL query
        cursor.execute("UPDATE link SET link = ?", (link,))

        # Save the changes to the database
        # Commit the changes made to the database
        db.commit()

    # If there is an error, log the error
    except sqlite3.Error as error:
        logger.error(f"Error adding link to database: {error}")


def get_link() -> list:
    """
    Retrieves a link from the database.
    Get a link from the database.

    Returns:
        list: A list of links from the database.

    Raises:
        sqlite3.Error: If there is an error with the database.
        sqlite3.Error: If there is a problem with the database.
        Exception: If there is an unexpected error.
    """
    try:
        # Connect to the database
        db = sqlite3.connect(DB_PATH)
        cursor = db.cursor()

        # Execute a SQL query to retrieve the link from the "link" table
        # Get the link from the database
        cursor.execute("SELECT link FROM link")

        # Commit the changes made to the database
        db.commit()

        # Fetch all the links from the database and return them
        link = cursor.fetchall()
        # link = link[0][0]
        return link

    # If there is an error, log the error
    except sqlite3.Error as error:
        logger.error(f"Error getting link from database: {error}")
