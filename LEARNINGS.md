1. What is the function of the following technologies in your assignment:

	i) HTML - Edit, position, and display the content such that text, images, and links to the client's browser.

	ii) CSS - Control over the desings of the content on the client's browser.

	iii) Javascript - Used for checking that the client input their name, e-mail, subject, and message to send in the contact page. If they leave some fields in a blank spance, they will get a warning message to fill the black. After they finishing to fill all fields, then the who messages will be sent.

	iv) Python - Handle the server requests POST and GET.

	v) Flask - Framework used in python to handle server requests.

	vi) HTTP - Used for format and transmission of messages and handle actions the web servers and browsers should take.

	vii) GET and POST requests - Used GET to obtain the html files(index, about, contact, blogs) of links. Used POST requests to send messages in the contact page. When whole input fields(name, e-mail, subject, message) are filled, the client can send a POST request to send this  data to the contact's email address.


2. How does HTML, CSS, and JavaScript work together in the browser in this assignment?

	- HTML displays the contents and CSS controls over the design of the contents on the webpage. In the assignment, the all pages have same color of background and font size and color of headers. And fix positions of the footer which contains the three links of the index, about, contact pages. Javascript handles the contact form to ensure that the client fills in all fileds completely the name, e-mail, subject, and message fields to send it in the contact page.


3. How does Python and Flask work together in the server for this assignment?

	- Python imports Flask, render_template, requestuses from Flask. So, we handled every requests from the server in Python while Flask running the server.


4. List all of the possible GET and POST requests that your server turns a response for and describes what happens for each GET and POST request:

	"GET /index HTTP/1.1" 200 - This means GET request gets the index.html file succefully through the route /index.

	"GET /blog/8-experiments-in-motivation HTTP/1.1" 200 - This means GET request gets the 8-experiments-in-motivation.html file succefully through the route /blog/8-experiments-in-motivation.

	"GET /blog/a-mindful-shift-of-focus HTTP/1.1" 200 - This means GET request gets the a-mindful-shift-of-focus.html file succefully through the route /blog/a-mindful-shift-of-focus

	"GET /blog/how-to-develop-an-awesome-sense-of-direction HTTP/1.1" 200 - This means GET request gets the how-to-develop-an-awesome-sense-of-direction.html file succefully through the route /blog/how-to-develop-an-awesome-sense-of-direction.


	"GET /blog/training-to-be-a-good-writer HTTP/1.1" 200 - This means GET request gets the training-to-be-a-good-writer.html file succefully through the route /blog/training-to-be-a-good-writer.

	"GET /blog/what-productivity-systems-wont-solve HTTP/1.1" 200 - This means GET request gets the what-productivity-systems-wont-solve.html file succefully through the route /blog/what-productivity-systems-wont-solve.

	"GET /about HTTP/1.1" 200 - This means GET request gets the about.html file succefully through the route /about.

	"GET /contact HTTP/1.1" 200 - This means GET request gets the contact.html file succefully through the route /contact.

	"POST /contact HTTP/1.1" 200 - This means POST request sends e-mail successfully.
