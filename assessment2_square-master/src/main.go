package main

import (
  "strconv"
  "log"
  "encoding/json"
	"net/http"
)

func square(write http.ResponseWriter, r *http.Request) {
  var varX []string //create initial variables

  if r.URL.Path != "/square" { //if the incorrect url
      http.Error(write, "404 not found.", http.StatusNotFound)
      json.NewEncoder(write).Encode("True")
      return
  }

  if r.Method != "GET" { //if not a get request
      http.Error(write, "Method is not supported.", http.StatusNotFound)
      json.NewEncoder(write).Encode("True")
      return
  }

  varX, err1 := r.URL.Query()["x"] //query the x value in the url parameters

  if !err1 || len(varX[0]) < 1  { //if we have error or the input length is less than 1
		log.Fatal(err1)
    json.NewEncoder(write).Encode("True")
    return
	}

  x, err := strconv.Atoi(varX[0]) //convert the parameters from string to int
	if err != nil {
		log.Fatal(err)
    json.NewEncoder(write).Encode("True")
    return
	}


  answer := Squared(x); //square the number

	write.Header().Set("Content-Type", "application/json")
  write.Header().Set("Access-Control-Allow-Origin", "*")

	json.NewEncoder(write).Encode(answer)
  //return the answer as json

}


func main() {

	http.HandleFunc("/square", square)

	if err := http.ListenAndServe(":80", nil); err != nil { //listen for port 80
		log.Fatal(err)
	}
}
