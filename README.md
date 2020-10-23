# Labs-Interview project

This porject was designed to provide a REST API that recommends friends for users in the database.

For this project it was used a combination of Django, DjangoRestFramework and SQLite3.

Documentation provided by Swagger

To run this project simply clone it and run the docker-compose file.

`docker-compose up -d`

The API documentation is provided by swagger and can be found at http://localhost:8000/api/schema/swagger-ui/

The project requested 4 endpoints:

1. Expose every Person in the database.
GET http://localhost:8000/api/users/


2. Expose every Friend of a given person in the database.
GET http://localhost:8000/api/friends/<str:name>


3. Expose a friend recommendation for a person in the database.
GET http://localhost:8000/api/users/<str:name>/recommendation


4. A way to register a new person informing it's new friends in the signup
POST http://localhost:8000/api/users/
body:
`
{
  "name": "name of the person",
  "friends": [
      "list of friends"
      ]
}
`
