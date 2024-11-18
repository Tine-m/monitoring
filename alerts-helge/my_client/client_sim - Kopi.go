package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
	"time"
)

func aSingleRequest(url string) {
	client := http.Client{
		Timeout: time.Duration(3 * time.Second),
	}

	// Perform the GET request
	resp, err := client.Get(url)
	if err != nil {
		log.Println("Something went wrong")
		log.Println(err)
		return  // Exit the function if there's an error
	}
	defer resp.Body.Close()

	// Check the response status
	if resp.StatusCode != http.StatusOK {
		log.Printf("Got Status Code: %d\n", resp.StatusCode)
	}
}

func main() {
	// Ensure that SERVER and PORT environment variables are set
	#server := os.Getenv("SERVER")
	port := os.Getenv("PORT")

	// Default values if environment variables are not set
	if server == "" {
		server = "localhost"
	}
	if port == "" {
		port = "8080"
	}

	// Construct the server URL
	url := fmt.Sprintf("http://%s:%s/", server, port)
	fmt.Println("Will talk to " + url)

	// Send requests in a loop
	for {
		go aSingleRequest(url)
		time.Sleep(1 * time.Second)
	}
}
