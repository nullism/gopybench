import falcon
import ujson

class Benchmark:

    def on_get(self, req, resp, name="World!"):
        resp.body = ujson.dumps({
            "myString": "Hello, %s"%(name),
            "myInt": 123,
            "myBool": True
        })


app = falcon.API()
app.add_route('/', Benchmark())
app.add_route('/{name}', Benchmark())
