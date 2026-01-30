package divide_main

import (
  "strconv"
  "log"
  "encoding/json"
	"net/http"
)

func Divide(write http.ResponseWriter, r *http.Request) {
  var varX, varY []string //create initial variables

  if r.URL.Path != "/divide" { //if the incorrect url
      http.Error(write, "404 not found.", http.StatusNotFound)
      return
  }

  if r.Method != "GET" { //if not a get request
      http.Error(write, "Method is not supported.", http.StatusNotFound)
      return
  }

  varX, err1 := r.URL.Query()["x"] //query the x value in the url parameters

  if !err1 || len(varX[0]) < 1  { //if we have error or the input length is less than 1
		log.Fatal(err1)
    return
	}

  x, err := strconv.Atoi(varX[0]) //convert the parameters from string to int
	if err != nil {
		log.Fatal(err)
    return
	}

  varY, err2 := r.URL.Query()["y"] //query the y value in the url parameters

  if !err2 || len(varY[0]) < 1  { //if we have error or the input length is less than 1
		log.Fatal(err1)
    return
	}

  y, err := strconv.Atoi(varY[0]) //convert the parameters from string to int
	if err != nil {
		log.Fatal(err)
    return
	}

  answer := divided(x,y); //divide the numbers

	write.Header().Set("Content-Type", "application/json")
  write.Header().Set("Access-Control-Allow-Origin", "*")

	json.NewEncoder(write).Encode(answer)
  //return the answer as json

}
