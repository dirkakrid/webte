import pkg_resources
import tornado.web


__version__ = pkg_resources.get_distribution(__package__).version


class RequestHandler(tornado.web.RequestHandler):

    pass


class ErrorHandler(RequestHandler, tornado.web.ErrorHandler):

    pass
