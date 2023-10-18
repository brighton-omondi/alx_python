import MySQLdb
import sys


def list_cities_of_state(username, password, database_name, state_name):
    try:
        # Connect to the MySQL server
        connection = MySQLdb.connect(
            host="localhost", port=3306, user=username, passwd=password, db=database_name)

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Define the SQL query with a parameterized query
        sql_query = "SELECT * FROM cities WHERE state_name = %s ORDER BY id ASC"

        # Execute the query with the state name as a parameter
        cursor.execute(sql_query, (state_name,))

        # Fetch all the results
        cities = cursor.fetchall()

        # Display the results
        for city in cities:
            print(city)

        # Close the cursor and the connection
        cursor.close()
        connection.close()

    except MySQLdb.Error as e:
        print("Error: {}".format(e))
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script_name.py <username> <password> <database_name> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    list_cities_of_state(username, password, database_name, state_name)
