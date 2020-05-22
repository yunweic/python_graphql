# Python Flask with GraphQL

Python Flask backend using Graphene for GraphQL query

## Set up environment

1.  Install Python3.7+
2.  cmd > `pip3 install -r requirements.txt`
3.  change .env file to set the environment for MySQL connection
4.  cmd > `source .env`

## Create MySQL table

1.  cmd > `python3 setup.py`

## Run web backend with GraphQL

1.  cmd > `python3 app.py`

## Access graphiql to test the GraphQL queries and mutations

1. Access graphiql sandbox by visiting http://127.0.0.1:5000
2. See the query and mutation format in the right panel