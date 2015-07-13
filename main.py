import web

from config import config, is_test
from urls import urls

import mongoengine

db = config.database

mongoengine.connect(
    db.get('db'), host=db.get('host'), port=db.get('port')
)

app = web.application(urls, globals())

""" Main HTTP status and error handler """
def error_handler(handler):
    try:
        handler()
    except web.webapi.OK as ex:
        return ex.data
    except web.webapi.Created as ex:
        return ex.data
    except web.HTTPError as ex:
        return ''

app.add_processor(error_handler)

if not is_test() and __name__ == "__main__":
    app.run()
else:
    webapp = app.wsgifunc()
