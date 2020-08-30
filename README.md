# Python Flask with GraphQL

Python Flask backend using Graphene for GraphQL query. It uses SQLAlchemy to interface with MySQL. Nginx, uWSGI, and supervisord is included for docker image.

## Set up environment

1.  Install Python3.7+
2.  cmd > `cd backend_graphql`
3.  cmd > `pip3 install -r requirements.txt`
4.  change .env file to set the environment for MySQL connection
5.  cmd > `source .env`

## Create MySQL table

1.  cmd > `python3 setup.py`

## Run web backend with GraphQL

1.  cmd > `python3 app.py`

## Access graphiql to test the GraphQL queries and mutations

1. Access graphiql sandbox by visiting https://127.0.0.1:5000
2. See the query and mutation format in the right panel

# Login application

Login REST API using Python Flask. It currently uses hardcoded credentials. Nginx, uWSGI, and supervisord is included for docker image.

## Set up environment

1. Install Python3.7+
2. cmd > `cd backend_login`
3. cmd > `pip3 install -r requirements.txt`
4. change .env file to set the environment for LOGIN_IP_ADDRESS and LOGIN_PORT connection. Make sure the URL and port doesn't clash with the GraphQL service.
5. cmd > `source .env`

## Run web backend for the login REST API

1.  cmd > `python3 app.py`

## Login to get JWT Token and Refresh expired token

1. Use the login and refresh REST API in the POSTMAN template
2. Change the url to point to the REST API server

# Deploy to AWS

## Manually build the login application into Docker image

1. docker build -t <IMAGE_NAME> <PATH_TO_DOCKERFILE>

## Continuous integraiton

1.  TravisCI will automatically build the docker image and upload to dockerhub once code is pushed to master