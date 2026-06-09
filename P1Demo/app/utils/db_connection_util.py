"""
I'm a util class. I store ugly and/or frequently used code. It's a living...
and a perfect example of Abstraction BTW.

This util has just 2 functions:

-Set up the database and table (we'll run this once in main)
-Get a connection to the database (we'll use this often in the repo layer)

This file is ⚠️ HARDCODING DATABASE CREDENTIALS ⚠️
What a *HORRIBLE IDEA* (unless you're just doing a little demo)
In a real app, you'd probably just use environment variables.
"""
import mysql.connector

# Runs once in main to make the Animals table and insert a record
def setup():
    # Connect WITHOUT a database first - we need to create one here
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password"
    )

    # Open a cursor, which allows us to execute SQL commands through the DB connection
    cursor = conn.cursor()

    # Now we can start executing DB commands:

    cursor.execute("CREATE DATABASE IF NOT EXISTS zoo")
    cursor.execute("USE zoo")

    # I didn't do much for constraints here. But you should :)
    # I also specified "PRIMARY KEY" but you don't have to.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS animals (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            species TEXT,
            weight FLOAT,
            height FLOAT,
            guest_rating FLOAT
        )
    """)

    cursor.execute("""
    INSERT INTO animals (name, species, weight, height, guest_rating) VALUES
    ('Fluffy', 'Lion', 200, 1.5, 4.5);
    """)

    cursor.execute("""
    SELECT * FROM animals
    """)

    results = cursor.fetchall()  # Store the results of the select!
    # Print em out just for console verification
    for row in results:
        print(row)

    conn.commit() # Save the changes made to the DB

    # Close the Cursor and Connection to save resources.
    cursor.close()
    conn.close()
    print("Database setup complete!")


# Runs every time we need a DB connection in the repo layer (which is once per method)
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="zoo"  # remove this line for DDL setup since DB may not exist yet
    )