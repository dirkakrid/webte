import tornado.testing
import webte.application


class TestCase(
        tornado.testing.AsyncHTTPTestCase,
        tornado.testing.LogTrapTestCase):

    def get_app(self):
        return webte.application.Application(debug=False)
