import psycopg2

# Establish a connection to the PostgreSQL database.
conn = psycopg2.connect(host="localhost",
                        database="postgres",
                        user="postgres",
                        password="admin",
                        port=5432)

# Create a cursor object.
# The cursor allows you to execute SQL commands and fetch results.
cur = conn.cursor()

# Execute a SQL command to create a table named 'person' if it doesn't already exist.
# The table has columns for id (primary key), name, age, and gender.
cur.execute("""CREATE TABLE IF NOT EXISTS person(
    id INT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    gender CHAR
);
""")

# Insert multiple rows of data into the 'person' table.
cur.execute("""INSERT INTO person (id, name, age, gender) VALUES
(1, 'Mike', 30, 'm'),
(2, 'John', 29, 'm'),
(3, 'Dennis', 28, 'f'),
(4, 'King', 21, 'm'),
(5, 'Dani', 40, 'f');
""")

# Select all columns from the 'person' table where the name is 'Dennis'.
cur.execute("""SELECT * FROM person WHERE name = 'Dennis';""")

# Fetch and print a single row from the result set.
# Since the query is expected to return only one row for 'Dennis', fetchone() is used.
print(cur.fetchone())

# Select all columns from the 'person' table where the age is less than 30.
cur.execute("""SELECT * FROM person WHERE age < 30;""")

# Iterate through all fetched rows and print only the name (second element, index 1) of each row.
for row in cur.fetchall():
    print(row[1])  # Only the name

# Use mogrify to safely format a SQL query with parameters.
# This prevents SQL injection vulnerabilities by properly escaping the input values.
# The query selects persons whose name starts with 'D' and are younger than 41.
sql = cur.mogrify(
    """SELECT * FROM person WHERE starts_with(name, %s) AND age < %s""", ("D", 41))

# Print the mogrified SQL query (for demonstration purposes).
print(sql)

# Execute the safely formatted SQL query.
cur.execute(sql)

# Fetch and print all remaining rows from the result set of the last query.
print(cur.fetchall())

# Commit the transaction to save the changes made to the database (table creation and data insertion).
conn.commit()

# Close the cursor. It's good practice to close cursors when they are no longer needed.
cur.close()

# Close the database connection. This releases the database resources.
conn.close()
