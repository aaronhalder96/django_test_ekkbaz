# Django App to get a list of businesses within 2000 km

System Requirements: Python Version >= 3.8.0

To clone the repository with HTTPS, use the following command in your desired directory:<br />
git clone https://github.com/aaronhalder96/django_test_ekkbaz.git

Before running the app, please install the packages mentioned in the requirements.txt file by using the following command:<br />
pip install -r requirements.txt

## Documentation

1. POST http://127.0.0.1:8000/register/   <br />
Creates a new user with the given username, email, and password <br />
Sample JSON data    <br />
{  <br />
    "username": "admin",  <br />
    "email": "admin@ekkbaz.com",  <br />
    "password": "admin123"  <br />
}

2. GET http://127.0.0.1:8000/api/token/ <br />
Returns 2 items: <br />
refresh: value of the token after the refresh button is clicked <br />
access: value of the token currently in use <br />
Sample JSON data    <br />
{  <br />
    "username": "admin",  <br />
    "password": "admin123"  <br />
}

3. GET http://127.0.0.1:8000/api/token/refresh/ <br />
Returns the value of the token currently in use <br />
Sample JSON data    <br />
{   <br />
    "refresh": "your_jwt_refresh_token <br />"
}

4. GET http://127.0.0.1:8000/business/   <br />
Returns a list of all business names and their respective locations. Use the access token in authorization (Type: Bearer Token)
Sample Output   <br />
{   <br />
    "businesses": [   <br />
        {   <br />
            "Google": 500   <br />
        },   <br />
        {   <br />
            "Netflix": 1948   <br />
        }   <br />
    ]   <br />
}

## Dockerization

1. To build the docker and install all necessary components, please use the following command: <br />
docker-compose build

2. To run the docker, please use the following command: <br />
docker-compose up

## CI/CD Pipeline

Unfortunately, I do not have an AWS Console account. I do not want to create a personal account. So I cannot proceed with this step. But 
I have included the pipeline.yaml file that is necessary for proceeding with this step.
