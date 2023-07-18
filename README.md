## Social Network


### Description:
On this service, users can post messages and rate other users' posts by giving them likes and dislikes. You cannot rate your own posts


### Template for filling .env file (create in a common directory)

DB_TYPE=postgresql                        _The PostgreSQL database used_
DB_DRIVER=asyncpg                         _Asynchronous driver_
POSTGRES_USER=postgres                    _Specify username_  
POSTGRES_PASSWORD=postgres                _Specify the password to connect to the database_  
DB_NAME=postgres                          _Specify the name of the created database_ 
DB_HOST=db                                _Specify the name of the service (container)_  
DB_PORT=5432                              _Specify the port to connect to the database_
SECRET=secret                             _Specify the secret key for hashing user passwords_ 
EMAIL_HUNTER_KEY=your_key                 _Specify API key for Email Hunter_


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
