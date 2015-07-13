#!/usr/bin/env python
# coding: utf-8

import web
import mongoengine

from model import Bird


class BirdsHandler:
    ''' Handler for Bird objects, used by BirdsController '''

    def __init__(self):
        pass

    """ Get all objects """
    def get_list(self):
        """
        ### Request `GET /birds`

        Empty body.

        ### Response

        Valid status codes:

          - `200 OK`

        The body is a JSON array based on the JSON schema can be found in
        `get-birds-response.json`.
        """

        birds = []

        # filter by visibility
        where = {'visible': True}

        # get items sorted by date added (desc)
        for bird in Bird.objects(**where).order_by('-added'):
            birds.append(self.format_bird(bird))

        return birds

    """ Get object by id """
    def get(self, uuid):
        """
        ### Request `GET /birds/{id}`

        Empty body.

        ### Response

        Valid status codes:

         - `200 OK` if the bird exists
         - `404 Not found` if the bird does not exist

        A `404 Not found` is expected when the bird does not exist, but not for
        birds with `visible` set to `false`.

        The response body for a `200 OK` request can be found in
        `get-birds-id-response.json`.

        """

        try:
            bird = Bird.objects.get(id=uuid)
            return self.format_bird(bird)

        except mongoengine.DoesNotExist:
            raise web.notfound()

        except mongoengine.ValidationError:
            raise web.notfound()

    """ Create new object """
    def create(self, data):
        """
        ### Request `POST /birds`

        The body is a JSON object based on the JSON schema can be found in
        `post-birds-request.json`.

         - If `visible` is not set, it should default to `false`.
         - `added` should default to today's date (in UTC)

        ### Response

        Valid status codes:

         - `201 Created` if the bird was successfully added
         - `400 Bad request` if any mandatory fields were missing or if the
               input JSON was invalid

        The body is a JSON object based on the JSON schema can be found in
        `post-birds-response.json`.

        """

        # try to create a new object
        try:
            bird = Bird()

            bird.name = data.get('name')
            bird.family = data.get('family')
            bird.continents = data.get('continents')
            bird.visible = data.get('visible', False)
            bird.added = data.get('added', None)

            bird.save()
            bird.reload()

            return self.format_bird(bird)

        except mongoengine.ValidationError:
            raise web.badrequest()

        except AttributeError:
            raise web.badrequest()

        except ValueError:
            raise web.badrequest()

    """ Delete object by id """
    def delete(self, uuid):
        """
        ### Request `DELETE /birds/{id}`

        Empty body

        ### Response

        Valid status codes:

         - `200 OK` if the bird has been removed
         - `404 Not found` if the bird didn't exist

        Empty body expected.

        """

        try:
            bird = Bird.objects.get(id=uuid)

        except mongoengine.DoesNotExist:
            raise web.notfound()

        except mongoengine.ValidationError:
            raise web.notfound()

        bird.delete()

    """ Return a dict suitable for output """
    def format_bird(self, bird):

        return dict({
            "id": bird.get_id(),
            "name": bird.name,
            "family": bird.family,
            "continents": bird.continents,
            "added": bird.get_date(),
            "visible": bird.visible
        })
