# gopybench

This is a simple benchmark of Go's `http` and various Python frameworks. 

## Execution

### 1. Start the server

Start the server on port 8000 using Gunicorn (-w 2) if a WSGI framework, or the built-in framework server in the case of Go and Tornado. 

*Note: No significant change was recorded by increasing the number of Gunicorn workers in my test environment.*

### 2. Apache Bench

Run `run-bench.sh <outputfilename>`. This just executes `ab -c 100 -n 10000 http://127.0.0.1:8000/FOO`, where name is a string value handled by each server's dispatch function.

### 3. Each test returns a JSON response

If using `run-bench.sh`, the url of `http://127.0.0.1/FOO`, you can expect a response of:

```
{
    myInt: 123,
    myBool: true,
    myString: "Hello, FOO"
}
```

