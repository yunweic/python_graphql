# Python Flask with GraphQL

Python Flask backend using Graphene for GraphQL query. It uses SQLAlchemy to interface with MySQL. Nginx, uWSGI, and supervisord is included for docker image.

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

## Manually build the Flask application into Docker image

1. docker build -t <IMAGE_NAME> <PATH_TO_DOCKERFILE>

## TravisCI will automatically build the docker image and upload to dockerhub once code is pushed to master

## TODO
1.  Add user authentication and authorizaiton to GraphQL queries and mutations