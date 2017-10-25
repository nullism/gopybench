from pycnic.core import WSGI, Handler

class Benchmark(Handler):

    def get(self, name="World"):
        return {
            "myString": "Hello, %s" % name,
            "myInt": 123,
            "myBool": True
        }


class app(WSGI):
    routes = [
        ("/", Benchmark()),
        ("/([\w]+)", Benchmark())
    ]
