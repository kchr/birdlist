#!/usr/bin/env python
# coding: utf-8

import json

from paste.fixture import TestApp
from nose.tools import *

from main import app

class TestBirdsApp():

    middleware = []
    test_app = None

    def __init__(self):
        self.test_app = TestApp(app.wsgifunc(*self.middleware))

    def test_index(self):

        # index page should always return 200
        r = self.test_app.get('/birds')
        assert_equal(r.status, 200)

        # content should be a json encoded list
        response = json.loads(r.body)
        assert_true(isinstance(response, list))

    def test_index_only_visible(self):

        # all entities in public index should have visible: True
        r = self.test_app.get('/birds', status=200)
        response = json.loads(r.body)

        for bird in response:
            assert_true(bird.get('visible'))

    def test_get_notfound(self):

        test_urls = ['/birds/123', '/birds/', '/birdz']

        # test a list of urls known to cause 404
        for url in test_urls:
            r = self.test_app.get(url, status=404)
            assert_equal(r.status, 404)

    def test_delete_notfound(self):

        r = self.test_app.delete('/birds/123', status=404)
        assert_equal(r.status, 404)

    def test_post_get_delete_ok(self):

        data = {
            "name": "Xyzzy",
            "family": "toucans",
            "visible": True,
            "continents": [1, 3]
        }

        # create a new entity, expect status 201
        request = json.dumps(data)
        r = self.test_app.post('/birds', request, status=201)
        assert_equal(r.status, 201)

        # check for Location: header with reference to new entity
        location = r.header('Location')

        # make sure id in response body matches reference in header
        response = json.loads(r.body)
        bird_id = response.get('id')
        assert_equal(location, '/birds/%s' % bird_id)

        # try to get the new entity
        r = self.test_app.get(location, status=200)
        assert_equal(r.status, 200)

        # make sure id from response matches
        response = json.loads(r.body)
        assert_equal(bird_id, response.get('id'))

        # delete the new entity, expect status 200
        r = self.test_app.delete(location, status=200)
        assert_equal(r.status, 200)

    def test_post_invalid_data(self):

        data = {
            "name": "Xyzzy",
            "family": "toucans",
            "visible": "yes",     # expects boolean
            "continents": [1, 3]
        }

        # try to create new entity with invalid data
        request = json.dumps(data)
        self.test_app.post('/birds', request, status=400)

    def test_post_missing_required(self):

        data = {
            "name": "Xyzzy"
        }

        # try to create new entity with missing required values
        request = json.dumps(data)
        self.test_app.post('/birds', request, status=400)

    def test_bad_methods(self):

        base_url = '/birds'

        # test PUT /birds
        r = self.test_app.put(base_url, status=405)
        assert_equal(r.status, 405)
