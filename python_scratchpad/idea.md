Load a JSON from an endpoint with employee data
https://s3.eu-west-2.amazonaws.com/interview.thanskben.com/backend/employees.json

Process all records in the file by writing the email and full name (first name +
last name) to a new local output CSV file (semicolon as separator)

If the full name exceeds 15 characters, shorten the full name by removing any
middle names and if not enough, reduce the first name to one character and a
dot. For example: "Benjamin Engman" -> "B. Engman" Set a header row with Email
and Short Full Name
