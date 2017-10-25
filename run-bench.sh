#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <output-file>"
    exit 1
fi

ab -c 100 -n 10000 http://127.0.0.1:8000/FOO > $1
