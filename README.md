## Social Network


### Description:
On this service, users can post messages and rate other users' posts by giving them likes and dislikes. You cannot rate your own posts


### Template for filling .env file (create in a common directory)

DB_TYPE=postgresql                        _(The PostgreSQL database used)_

DB_DRIVER=asyncpg                         _(Asynchronous driver)_

POSTGRES_USER=postgres                    _(Specify username)_

POSTGRES_PASSWORD=postgres                _(Specify the password to connect to the database)_

DB_NAME=postgres                          _(Specify the name of the created database)_

DB_HOST=db                                _(Specify the name of the service (container))_

DB_PORT=5432                              _(Specify the port to connect to the database)_

SECRET=secret                             _(Specify the secret key for hashing user passwords)_

EMAIL_HUNTER_KEY=your_key                 _(Specify API key for Email Hunter)_



### Installation and usage

1. Install Docker and docker-compose appropriate for your operating system (follow the instructions for installing the console and desktop versions on the official websites)

2. Start the project with the command in console:
`docker-compose up`

3. The API specification (Swagger) will be available at http://localhost:8000/docs/

4. You can use Swagger for creating users, publish and react posts

Note: All email addresses are verified through Email Hunter on existence. Use real emails to register users


### API
The API request specification and list of endpoints are available at (the project should be launched):
http://localhost:8000/docs/


### Python version
`3.11.3`

The dependencies are presented in the file `requirements.txt`


### Technology Stack
`FastAPI` `SQLAlchemy` `PostgreSQL` `Pydantic` `Alembic` `Docker` `docker-compose`


### Author
_Max Stepanov_  
_GitHub: NewZealandMax_
