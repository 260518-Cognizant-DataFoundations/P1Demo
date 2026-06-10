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

# The DB setup function (called once in main)
def setup():
    # Create/Connect to the database, then create a table
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password"
    )

    # Open a cursor, which allows us to execute SQL commands via the DB Connection
    cursor = conn.cursor()

    # Now that we have a cursor, let's create the DB, a table, and do some DML
    cursor.execute("CREATE DATABASE IF NOT EXISTS zoo")
    cursor.execute("USE zoo")

    # Create the animals table (should DIRECTLY mirror the Animal Class)
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

    # Insert an animal record then select it
    cursor.execute("""
    INSERT INTO animals (name, species, weight, height, guest_rating)
    VALUES ("Fluffy", "Lion", 200, 1.5, 4.5)
    """)

    cursor.execute("SELECT * FROM animals")

    # Have to store the results of a select or an error occurs
    results = cursor.fetchall()
    print(results)

    # CLEAN UP! (We'll do this often). We need to save and close everything
    conn.commit()
    cursor.close()
    conn.close()
    print("DB Setup Complete!")


# The connection function (the repo layer will use this to access the DB)
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="zoo" # WILL FAIL HERE IF YOU HAVEN'T RUN setup()
    )