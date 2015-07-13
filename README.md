Birdlist v0.1
=============

Small HTTP/JSON server with REST interface for managing a database of birds.

It is written in Python, using the minimalist web.py framework and mongoengine
as MongoDB storage interface. See below for instructions on how to configure
and run, along with some client examples.

The server logs all incoming requests (and response codes) to STDOUT.

Prerequisities
--------------

You will need a MongoDB instance running somewhere within reach.

Requirements
------------

Python packages:

  - web.py `(<= 0.37)`
  - mongoengine `(<= 0.10.0)`

Read further down (*Installation*) on how to install required packages.

Installation
------------

Clone this repository to a location of your choice:

    $ git clone https://github.com/kchr/birdlist

To install required packages, run:

    $ make prod

Testing
-------

If you want to run tests you will need some dev packages too:

    $ make dev

To run the suite of tests:

    $ make tests

See *Configuration* below on how to specify database host and port.

Usage
-----

Start the HTTP/JSON server:

    $ make serve

This will spawn a HTTP server on localhost port 8080, answering to requests prefixed with `/birds`.

See *Configuration* below on how to specify listening interface and port.

Make HTTP requests using your favorite client!

Configuration
-------------

**Environment variables**

    WEBPY_LISTEN      [127.0.0.1:8080]    Interface and port for HTTP/JSON server
    MONGODB_HOST      [127.0.0.1:27017]   Hostname and port for mongodb instance
    MONGODB_DB        [birds]             Database name for collection

Environment variables can be exported or just passed along the command line.

Therefore,

    $ export MONGODB_HOST=10.0.0.1:27017
    $ make tests

...has the same effect as:

    $ MONGODB_HOST=10.0.0.1:27017 make tests

**Setting the environment**

To make it serve on another interface or port, set `WEBPY_LISTEN` in your environment:

    $ WEBPY_LISTEN=0.0.0.0:8080 make serve 

By default, it will try to reach a MongoDB instance running on localhost port 27017.

To change this, set `MONGODB_HOST` in your environment:

    $ MONGODB_HOST=10.0.0.1:31337 make serve 


Client examples
---------------

Recommended clients:

  - [cURL](http://curl.haxx.se/)
  - [wget](http://www.gnu.org/software/wget/)
  - Chrome: [Advanced REST client](https://chrome.google.com/webstore/detail/advanced-rest-client/hgmloofddffdnphfgcellkdfbfbjeloo)
  - Firefox: [HttpRequester](https://addons.mozilla.org/en-US/firefox/addon/httprequester/)

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
