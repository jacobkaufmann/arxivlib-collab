import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("arxivlib collab server\n")

def make_api():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

def main():
    api= make_api()
    api.listen(8080)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
