import webte


class IndexHandler(webte.RequestHandler):

    def get(self):
        self.render("index.html")
