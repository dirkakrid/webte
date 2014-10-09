import copy
import pkg_resources
import tornado.web
import webte.index
import webte.terminal


class Application(tornado.web.Application):

    routes = [
        (r"/?", webte.index.IndexHandler),
        (r"/terminal/?", webte.terminal.TerminalWebSocket),
        (r".*", webte.ErrorHandler, {"status_code": 404}),
    ]

    settings = {
        "template_path": pkg_resources.resource_filename("webte", "templates"),
        "static_path": pkg_resources.resource_filename("webte", "static"),
    }

    def __init__(self, debug=False, **kwargs):
        settings = copy.deepcopy(self.settings)
        settings.update(kwargs)
        super().__init__(self.routes, debug=debug, **settings)
