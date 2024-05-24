### Simple CRUD with FastAPI and SQLAlchemy

#### Steps to run it
1. create a python venv  using the command `python -m venv myenv` and activate it using `myenv\Scripts\activate`
2. Install the dependencies: `pip install fastapi uvicorn SQLAlchemy alembic psycopg2-binary`
3. To run locally, create a postgres container with docker using the following command: `docker run --name <container_name> -e POSTGRES_PASSWORD=<password> -d -p 5432:5432 postgres:alpine`
4. create a .env file and add the following `postgresql://postgres:<password>@localhost:5432/postgers`
5. run the server: `uvicorn main:app --reload`
