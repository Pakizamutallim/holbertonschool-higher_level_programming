#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and database name from command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        charset="utf8"
    )

    # Create a cursor object to execute queries
    cur = db.cursor()

    # Execute the query to select all states
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the results
    query_rows = cur.fetchall()

    # Print the results
    for row in query_rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
