package main

import (
    "encoding/json"
    "log"
    "net/http"
    "github.com/gorilla/mux"
    "fmt"
)

type Message struct {
    MyInt       int   `json:"myInt"`
    MyString    string   `json:"myString,string"`
    MyBool      bool    `json:"myBool"`
}

func Benchmark(w http.ResponseWriter, req *http.Request) {
    params := mux.Vars(req)
    name := "World!"
    if len(params["name"]) > 0 {
        name = params["name"]
    }
    message := Message{
        MyInt: 123,
        MyString: fmt.Sprintf("Hello, %s", name),
        MyBool: true}
    json.NewEncoder(w).Encode(message)
}

func main() {
    router := mux.NewRouter()
    router.HandleFunc("/", Benchmark).Methods("GET")
    router.HandleFunc("/{name}", Benchmark).Methods("GET")
    log.Fatal(http.ListenAndServe(":8000", router))
}
