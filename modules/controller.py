#!/usr/bin/env python
# coding: utf-8

import web
import json

from handlers.birds import BirdsHandler


class BirdsController:
    ''' Controller for (JSONized) HTTP requests to BirdsHandler '''

    handler = None

    def __init__(self):
        web.header('Content-Type', 'application/json')
        self.handler = BirdsHandler()

    def GET(self, uuid=None):

        if uuid is None:
            data = self.handler.get_list()
        else:
            # @throws web.notfound
            data = self.handler.get(uuid)

        raise web.ok(self.dump_json(data))

    def POST(self, uuid=None):

        if uuid:
            raise web.badrequest()

        try:
            data_json = web.data()
            data = json.loads(data_json)

        except Exception:
            raise web.badrequest()

        # @throws web.badrequest
        bird = self.handler.create(data)

        # show reference to new entity, as per RFC 2616
        headers = {'Location': '/birds/%s' % bird.get('id')}

        raise web.created(self.dump_json(bird), headers)

    def DELETE(self, uuid=None):

        if uuid is None:
            raise web.badrequest()

        # @throws web.notfound
        self.handler.delete(uuid)

        raise web.ok()

    def dump_json(self, data):
        return json.dumps(data)
