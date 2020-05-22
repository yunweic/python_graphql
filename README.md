# Python Flask with GraphQL

Python Flask backend using Graphene for GraphQL query

## Set up environment

1.  Install Python3.7+
2.  cmd > `pip3 install -r requirements.txt`
3.  change .env file to set the environment for MySQL connection
4.  cmd > `source .env`

## Migrate MySQL database schema steps if needed

1.  cmd > `flask db init`
2.  cmd > `flask db -m migrate "my message"`
3.  cmd > `flask db upgrade`

## Run fraud detection web backend

1.  cmd > `python3 app.py`