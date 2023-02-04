import psycopg2
# Importing the library

# Connecting to the library
connection = psycopg2.connect(database="chinook")

# The cursor is what 'moves around' the DB
cursor = connection.cursor()

# Query 1
# cursor.execute('SELECT * FROM "Artist"')
# SQL query must be in single quotes 


# Query 2
# cursor.execute('SELECT "Name" FROM "Artist"')
# SQL query must be in single quotes


# Query 3
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])
# SQL query must be in single quotes,
# We are using a Python placeholder here and then specifying what the value is
# There are lots of these and they can be used to make queries more complex

# Query 4
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])
# SQL query must be in single quotes,

# Query 5
cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])
# SQL query must be in single quotes,
# Referencing another record using the Artist ID

# Query 6
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])
# SQL query must be in single quotes,

# Get all of the records in the table
# results = cursor.fetchall()


# Get a single result back from the table
results = cursor.fetchone()


# Connection needs to be closed once we have done what we need
connection.close()


# Print the results

for result in results:
    print(result)
