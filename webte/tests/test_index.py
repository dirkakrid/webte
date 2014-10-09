import webte.tests


class IndexHandlerTest(webte.tests.TestCase):

    def test_get(self):
        res = self.fetch("/", follow_redirects=False)
        self.assertEqual(res.code, 200)
        self.assertEqual(res.headers["Content-Type"],
                         "text/html; charset=UTF-8")
