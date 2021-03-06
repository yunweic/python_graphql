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

1. Access graphiql sandbox by visiting http://127.0.0.1:5000
2. See the query and mutation format in the right panel
3. All the GraphQL mutation needs to have an authorization header that consist of valid JWT Token. Query doesn't need a JWT Token
4. To get a valid JWT token, use the login REST API desribed in the sectino below.

# Login application

Login REST API using Python Flask. It currently uses hardcoded credentials. Nginx, uWSGI, and supervisord is included for docker image.

## Set up environment

1. Install Python3.7+
2. cmd > `cd backend_login`
3. cmd > `pip3 install -r requirements.txt`
4. change .env file to set the environment for LOGIN_IP_ADDRESS, LOGIN_PORT, SECRET_KEY, JWT_SECRET_KEY. Make sure the URL and port doesn't clash with the GraphQL service if run locally.
5. cmd > `source .env`

## Run web backend for the login REST API

1.  cmd > `python3 app.py`

## Login to get JWT Token and Refresh expired token

1. Change the url to point to the REST API server
2. Use the login and refresh REST API in the POSTMAN template
3. username: yunwei
4. password: password

# CI/CD

## Manually build the login application into Docker image locally

1. docker build -t <IMAGE_NAME> <PATH_TO_DOCKERFILE>

## Continuous integraiton

1.  TravisCI will automatically build the docker image and upload to dockerhub once code is pushed to master on GitHub

## deploy each service (reverseproxy-svc, svc-graphql-login, svc-graphql) to AWS EKS

1. cmd > `kubectl apply -f deployment.yaml` to deploy pods on AWS EKS
2. cmd > `kubectl get pods` to check the newly deployed pods on AWS EKS
3. cmd > `kubectl apply -f service.yaml` to deploy service on AWS EKS
4. cmd > `kubectl get services` to check the newly deployed services on AWS EKS

## Verify the service is working

1. cmd > `kubectl port-forward service/reverseproxy-svc 8080:8080` to make the service accessible locally
2. use the url if request is going through reverse proxy: `http://127.0.0.1:8080/api/v0/graphql` or `http://127.0.0.1:8080/api/v0/user/<login_or_refresh>`
3. cmd > `kubectl port-forward service/svc-graphql 8100:443 ` to make the graphql service accessible locally
4. use https if request is going directly to graphql: `https://127.0.0.1:8100/graphql`
5. cmd > `kubectl port-forward service/svc-graphql-login 8101:443 ` to make the graphql-login service accessible locally
6. use https if request is going directly to graphql-login: `https://127.0.0.1:8100/<login_or_refresh>`

# TODO in the future
1. Add user management REST API like create/update/delete user
2. Put user information into a database
3. Set up SSL termination at the reverse proxy
4. Add unit test

