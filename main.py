import sys
import web

from config import db, is_test
from urls import urls


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

try:
    if not is_test() and __name__ == "__main__":
        app.run()
    else:
        webapp = app.wsgifunc()
except KeyboardInterrupt:
    print "Exiting by user SIGINT"
    sys.exit()
