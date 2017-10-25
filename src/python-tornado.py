#!/usr/bin/env python3
import tornado.ioloop
import tornado.web

class Benchmark(tornado.web.RequestHandler):
    def get(self, name="World!"):
        self.write({
            "myString":"Hello, %s"%(name),
            "myInt": 123,
            "myBool": True
        })

app = tornado.web.Application([
    (r"/", Benchmark),
    (r"/(?P<name>[^\/]+)?", Benchmark)
])

if __name__ == "__main__":
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
