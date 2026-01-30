# Cloud Hosted Calculator
Cloud based calculator with each function in a different programming language, and hosted at the time on various different cloud platforms. 
This was done as a university project.

# Functions breakdown:


## Multiply
Using Python3 and flask, it reads in the arguments from the URL and parses out the x and y values into variables for multiplication. This is also packaged using docker and it was uploaded via the repository to rancher. It has error handling with a try except, if there is an error then we pass back an error value which gets displayed on the calculator using the frontend. The service runs on port 80.
### Testing:
We have automated CI testing with unit tests to ensure the function worked as expected and manual testing to ensure we received the proper errors on invalid inputs (e.g., no input or not a number).

## Divide
Implemented using Functions as a service method, using Go within. It is hosted on Google cloud platform and also allows for port 80 methods. It uses the URL.Query() function to read in the input http request, to parse out the individual x and y data passed in. It divides and then returns the answer encoded as json. For error handling we check the URL path is correct, it is a GET request, the values passed in are not empty and that they can be properly converted to an integer value.
### Testing:
Features automated testing with Gitlab CI for unit tests of the dividing function. Manual tests were used to ensure that errors were correctly being thrown for the provided checks on URL path, if it is a get request, non-integer values and that we had data input.

## Square
Using Go/Golang, it will only need to receive one input to square the number and return it to the user. Similar to the above it uses the URL.Query() function to read in the http incoming request, we parse out the data passed in, square it, and return as json. The error handling is also similar, the values are correct (not empty and a number), the request is a GET request and the URL path is correct.
### Testing:
Using Gitlab CI for automated unit test as well to ensure the function returned the correct squared number. Ensured the error handling worked correctly for non-valid input with manual testing as well.

## Modulo
Using ruby on rails I take in the data from the URL using: x = params[:x].to_i
(parameters to integer for the parameter x). I check for a y=0 error in case of dividing/modulo by 0. After using the modulo function against the data input, it is returned rendered as json.
### Testing:
As mentioned above I checked for y=0, which was discovered during manual testing to prevent any unhandled errors, if y is 0, we simply return 0. I also managed to get Gitlab CI automatic testing working for this function, which tests that the function is working correctly for positive and negative values.

## Proxy
I coded this in python, from the frontend I passed in a 3rd argument “operator” with each request to a function, the proxy would then use a switch statement to grab the correct URL for each operator, request the output from the URL and pass it back to the frontend. 
This used try catch statements and validated the inputs to ensure they existed.
<img width="940" height="743" alt="image" src="https://github.com/user-attachments/assets/9c466bf1-0262-42c4-be7d-e754a6ad8328" />
<img width="940" height="148" alt="image" src="https://github.com/user-attachments/assets/d64dd4e1-394f-46f4-bc3e-74bb6ce3432b" />

## Frontend service failure handler
Within the proxy container I implemented the failure handler. It would query a URL using dummy data and check the status code, if the status code were incorrect then we would use a backup hostname endpoint that was created in rancher using ingress. This also was used for the FaaS and I have a second endpoint for this as well in case the first were to go down.
<img width="940" height="122" alt="image" src="https://github.com/user-attachments/assets/efddc7d9-3b9a-4dc4-afac-4baffa108ddf" />


List of all URLs, backup and main


<img width="940" height="321" alt="image" src="https://github.com/user-attachments/assets/962d13e3-8f78-4406-975b-7dcdd35b9338" />


# Other notable checks:
## Frontend error handling 
Added in terms of allowing errors to be returned and displayed as an alert, and to check that the HTTP status is not outside an abnormal range.
<img width="940" height="392" alt="image" src="https://github.com/user-attachments/assets/e16b83b0-2f0d-4897-b03b-61550bbfc3c0" />

## Backend error handling
For the subtract function I added in a try catch function to handle any errors, allowing an error to be passed back to the frontend and displayed to the user via an alert box. I also checked the inputs for ‘not a number’ and if the input data was empty, returning 0.


<img width="940" height="631" alt="image" src="https://github.com/user-attachments/assets/55c678ca-fd46-4f23-8f16-0d6a55bdcade" />
<img width="441" height="131" alt="image" src="https://github.com/user-attachments/assets/edd752fe-1f14-4d3c-bc2f-56107ca195c7" />


For the add function I similarly used a try catch for general error handling, allowing an error message to be returned and alerted to the user on the frontend, as well I checked the inputs were numeric to ensure that letters or non-numbers were not going to be added and cause an error.


<img width="688" height="648" alt="image" src="https://github.com/user-attachments/assets/4ab438a7-a128-41d4-97cf-3422dc3a58a8" />
<img width="456" height="164" alt="image" src="https://github.com/user-attachments/assets/30583172-0840-4344-ab23-b041534de544" />

## Static configuration of routes to services in the frontend
Used in conjunction with the proxy, I used a switch statement for static routes on the front end, allowing for easy addition of new operators when passing through to the proxy.


<img width="467" height="570" alt="image" src="https://github.com/user-attachments/assets/4f3d851c-a230-41c7-8b12-d96d8b761a22" />


Example usage when calling a URL 


<img width="940" height="105" alt="image" src="https://github.com/user-attachments/assets/37f1c55f-2366-47d3-8692-32c16ed6cb21" />

## CI Testing HTTP request to check web API functionality
In the subtract Gitlab CI I call the server to be ran and perform a curl operation against it
<img width="433" height="418" alt="image" src="https://github.com/user-attachments/assets/5531035e-face-4b22-a2e8-7653744fa800" />


## Stateful saving and recovery 
I implemented this within my proxy docker container, it features a dictionary that saves the data input and outputs the index that a user can then input later to view the data they saved.


I initially check if the operator input is either “save” or “load”, then access the following functions.


<img width="940" height="150" alt="image" src="https://github.com/user-attachments/assets/97093512-5dcd-4bca-a921-860db4b91f83" />
<img width="940" height="328" alt="image" src="https://github.com/user-attachments/assets/7d4346f9-efc0-43ee-9243-c035cdcd946d" />


If save is chosen, we input the data at the current length (returned in 1 based indexing, so always 1 ahead of the latest saved position), and then return the index to the frontend that the user would type to access the data.
For loading we check the data input is actually present within the dictionary, if so, we return the number that was saved by calling the index to the frontend to display to the user, if the data is not present we return a default 0.

# Design

<img width="1179" height="1070" alt="image" src="https://github.com/user-attachments/assets/cfd37bd1-a060-4483-920d-5c547f45fea7" />

This is my design for a multiple cloud vendor option for the web calculator deployment.
For maximum resilience to both manmade and natural disasters, I chose two different cloud providers and both in different regions of the world, ensuring that if one region were to suffer from some kind of issue, the other is unlikely to also simultaneously, along with performance increases depending on what region of the world you are accessing this from.

For my design I chose 2 load balancers that was fully connected to both monitoring services (so an admin can review the alerts and reports of both environments), access to the proxy and frontend as they can choose how to best balance the requests between which environment has the best performance at that moment.
The monitoring service is connected to the proxy as all data would typically pass through there, and it saves its data to a separate store. This data then gets backed up to the cloud storage.

The proxy service has access to each math function in its cloud environment for passing all the requests along and back and is also used for stateful saving as per my above design, this data could then be ideally saved to a master database on the QPC, and replicated to the Google private cloud as well, and likewise stored elsewhere as a backup.

In terms of backups, I chose to use a snapshot backup as these are very easy to use for recovery purposes, and also using an incremental backup system for in between snapshots to minimise data loss should failure occur.

A reason I picked google private cloud is because they offer scalability, so if we are ever getting massive amounts of calculations, they offer the ability to scale up resources and ensure that no one is left without their calculation being completed, or without a long wait.

Overall, I believe this is a good cloud architecture as we have good redundancy measures across different sites, load balancers ensure that one cloud vendor is not going to be massively overused, and we should be able to easily use our calculator wherever we may go.






