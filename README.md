# URL Shortener

## Technologies used
- Python Flask Microframework for the backend
- Reacr for the frontend
- Postgres for the database
- Docker and docker-compose for the setup

## Folder Structure 
- All backend code is in the folder named backend and all frontend code is the folder named frontend.

## Running the Application Locally
The setup uses docker and docker-compose, please ensure that you have them setup on your local machine.

Run `make server` to start the application, this will also in turn run `make setup`

Run `make test` to run tests.

Run `make clean` to remove all images created.

While the applications is running:
- The API can be accessed at http://localhost:5000
- The frontend can be accessed at http://localhost:3000
