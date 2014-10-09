import unittest
import unittest.mock
import os
import pkg_resources
import webte
import webte.tests


dist = pkg_resources.get_distribution("webte")
main = dist.load_entry_point("console_scripts", "webte")


class MainTest(webte.tests.TestCase):

    @unittest.mock.patch("tornado.ioloop.IOLoop.instance")
    @unittest.mock.patch("webte.application.Application")
    def test_main(self, Application, instance):
        self.assertEqual(main(), 0)
        Application().listen.assert_called_once_with("7000")
        instance().start.assert_called_once()

    @unittest.mock.patch("tornado.ioloop.IOLoop.instance")
    @unittest.mock.patch("webte.application.Application")
    @unittest.mock.patch("builtins.print")
    def test_main_interrupt(self, print, Application, instance):
        instance().start.side_effect = KeyboardInterrupt()
        self.assertEqual(main(), 0)
        Application().listen.assert_called_once_with("7000")
        instance().start.assert_called_once()


class DistributionTest(webte.tests.TestCase):

    def test_version(self):
        self.assertEqual(webte.__version__, dist.version)
        self.assertRegex(webte.__version__, r'\d+\.\d+\.\d+')

    def test_package_data(self):
        def tree(directory):
            for path, dirs, files in os.walk(directory):
                for i in (os.path.join(path, i) for i in files):
                    yield i
        sources = list(dist.get_metadata_lines("SOURCES.txt"))
        for directory, _ in (os.path.split(i) for i in sources):
            for f in tree(directory):
                (self.fail("Untracked file in distribution: " + f)
                 if f not in sources
                 and not f.endswith(".pyc")
                 and not f.endswith(".py") else None)
