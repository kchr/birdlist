Birdlist v0.1
=============

Small HTTP/JSON server for managing a MongoDB database of birds.

Requirements
------------

Python packages:

  - web.py
  - mongoengine

You will also need a MongoDB instance running somewhere within reach.

Installation
------------

To install required packages, run:

    $ make prod

Testing
-------

If you want to run tests you will need some dev packages too:

    $ make dev

To run the suite of tests:

    $ make tests

Usage
-----

Start the HTTP/JSON server:

    $ make serve

This will spawn a HTTP server on localhost port 8080, answering to requests prefixed with `/birds`.

To make it serve on another interface or port, set `WEBPY_LISTEN` in your environment:

    $ WEBPY_LISTEN=0.0.0.0:8080 make serve 

By default, it will try to reach a MongoDB instance running on localhost port 27017.

To change this, set `MONGODB_HOST` in your environment:

    $ MONGODB_HOST=10.0.0.1:31337 make serve 

Make HTTP requests using your favorite client!

Client examples
---------------

Some examples for cURL:

    # list all visible birds
    $ curl -i -X GET http://localhost:8080/birds

    # post new bird
    $ curl -i -X POST --data "<json>" http://localhost:8080/birds

    # get bird by id
    $ curl -i -X GET http://localhost:8080/birds/<id>

    # delete bird by id
    $ curl -i -X DELETE http://localhost:8080/birds/<id>


API Specification
-----------------

       GET /birds                     List all birds (that are visible)
      POST /birds      [request]      Create new bird
       GET /birds/<id>                View specific bird object
    DELETE /birds/<id>                Remove specific bird object

Schema details for the JSON protocol can be found in doc/schema.