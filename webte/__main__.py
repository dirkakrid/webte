import sys
import tornado.ioloop
import tornado.autoreload
import tornado.options
import webte.application


tornado.options.define(
    "port", default="7000", help="http port number")
tornado.options.define(
    "debug", default=False, help="enable debugging")


def main():
    tornado.options.parse_command_line()
    application = webte.application.Application(
        debug=tornado.options.options.debug)
    application.listen(tornado.options.options.port)
    try:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        return 0
    return 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
